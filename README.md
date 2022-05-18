# Send Atlas Scientific water quality sensor readings via LoRaWAN

Reads Atlas Scientific EZO water quality sensors, and sends their readings over LoRaWAN via a Dragino Raspberry Pi hat.

## Software

Based on:

* [Whitebox Raspbeery EZO](https://github.com/whitebox-labs/whitebox-raspberry-ezo)
* [Dragino](https://github.com/BNNorman/dragino-1)

## Instructions

* Initialise the submodules: `git submodule update --init`
* Follow the [Dragino](https://github.com/BNNorman/dragino-1#installation-compute-nodes-version) installation instructions
* Follow the [Whitebox Raspbeery EZO](https://github.com/whitebox-labs/whitebox-raspberry-ezo#i2c-mode) installation instructions
* Copy `dragino.toml` from the `Dragino` directory to the root of this repo
* Run `python3 water_quality.py`
* Watch for output

### Data format

Data will be sent via TTN in the format: `DO:38.29,421.1|ORP:96.1|pH:14.000|EC:0.00,0,0.00,1.000|RTD:-1023.000`

## Disclaimer

I don't have any of the hardware, so your milage may vary.
