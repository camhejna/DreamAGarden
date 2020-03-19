# **Dream A Garden** #

![version]
![python-version]

Another IOT Garden. Built on a Raspberry Pi. [Powered by Dark Sky](https://darksky.net/poweredby/).

<img src="https://darksky.net/dev/img/attribution/poweredby-oneline.png"
alt="Powered by Dark Sky" width="200">

## Getting Started ##

Run the following from the repository root directory to install the needed dependencies.

```shell
# The minimum dependencies needed to run weatherBot
pip3 install -r requirements.txt
# Additional dependencies needed for testing, linting, and validating
pip3 install -r requirements-dev.txt
```

## Dependencies ##

* [darkskylib](https://github.com/lukaskubis/darkskylib) - a python library for
the [Dark Sky API](https://darksky.net/dev/docs).

* [Adafruit IO](https://github.com/adafruit/Adafruit_IO_Python) - a python
library for the [Adafruit IO API](https://io.adafruit.com/api/docs/#adafruit-io-http-api).

* [Adafruit Seesaw](https://github.com/adafruit/Adafruit_CircuitPython_seesaw)

## I/O Components ##

* [Adafruit Soil Sensor](https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/overview)

* [AM2302 (wired DHT22) temperature-humidity sensor](https://learn.adafruit.com/dht)

## General Resources ##

* [Soldering 101](https://www.instructables.com/id/Soldering-101-for-the-Beginner/)

* [Adafruit IO Basics](https://learn.adafruit.com/series/adafruit-io-basics)

* [Raspberry Pi SSH for MacOS](https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md)

[version]: https://img.shields.io/badge/v-0.1-blue
[python-version]: https://img.shields.io/badge/python-3.8.2-yellow
