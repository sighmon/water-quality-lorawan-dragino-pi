#!/usr/bin/env python3
"""
    Read Atlas Scientific water quality sensors
    and send their readings over LoRaWAN via a
    Dragino Raspberry Pi hat.
    Adheres to a 1% duty cycle
    cache.json will be created if it doesn't exist

    Based on:
    * https://github.com/whitebox-labs/whitebox-raspberry-ezo
    * https://github.com/BNNorman/dragino-1
"""
import logging
from time import sleep

import RPi.GPIO as GPIO
from AtlasI2C import (
    AtlasI2C
)
from dragino import Dragino


GPIO.setwarnings(False)

# add logfile
logLevel = logging.DEBUG
logging.basicConfig(
    filename="test.log",
    format='%(asctime)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s',
    level=logLevel,
)


def get_ezo_devices():
    """Returns a list of EZO devices."""
    device = AtlasI2C()
    device_address_list = device.list_i2c_devices()
    device_list = []

    for i in device_address_list:
        device.set_i2c_address(i)
        response = device.query("i")

        # check if the device is an EZO device
        checkEzo = response.split(",")
        if len(checkEzo) > 0:
            if checkEzo[0].endswith("?I"):
                # yes - this is an EZO device
                moduletype = checkEzo[1]
                response = device.query("name,?").split(",")[1]
                device_list.append(
                    AtlasI2C(
                        address=i,
                        moduletype=moduletype,
                        name=response,
                    )
                )
    return device_list


def get_data_from_all_ezo_devices(device_list):
    """Returns a list of string output from all EZO devices."""
    output = []
    for device in device_list:
        device.write("R")
        sleep(device.long_timeout)
    for device in device_list:
        output.append(device.read())
    return output


def main():
    """Gets a list of connected EZO devices, and sends their data via TTN."""
    print("\nConnected EZO devices:")
    ezo_device_list = get_ezo_devices()
    for device in ezo_device_list:
        print("\n" + device.get_device_info())

    # Create a Dragino object and join to TTN
    print("\nStarting dragino connection to TTN")
    D = Dragino("dragino.toml", logging_level=logLevel)
    D.join()

    print("\nWaiting for JOIN ACCEPT")
    while not D.registered():
        print(".", end="")
        sleep(2)
    print("\nJoined")

    while True:
        data = get_data_from_all_ezo_devices(ezo_device_list)
        # Not sure what the data looks like,
        # so let's concatenate it separated by "|"
        joined_data = "|".join(data)
        print("Sending data from devices: " + joined_data)
        D.send(joined_data)

        while D.transmitting:
            sleep(0.1)
        sleep(99*D.lastAirTime())  # limit to 1% duty cycle


if __name__ == '__main__':
    main()
