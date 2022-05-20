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

## Output data format

Data will be sent as `|` separated strings, with the name of the sensor and the data separated by `:`.

e.g. `DO:38.29,421.1|ORP:96.1|pH:14.000|EC:0.00,0,0.00,1.000|RTD:-1023.000`

## Chripstack decoder

To decode the messages received by [Chirpstack](https://www.chirpstack.io), use the decoder: [decode.js](decode.js)
