# **Dream A Garden** #

![version]
![python-version]

Another IOT Garden. Built on a Raspberry Pi. [Powered by Dark Sky](https://darksky.net/poweredby/).

<img src="https://darksky.net/dev/img/attribution/poweredby-oneline.png"
alt="Powered by Dark Sky" width="200">

## Getting Started ##

Run the following from the repository root directory to install the needed dependencies.

```sh
# The minimum dependencies needed to run weatherBot
pip3 install -r requirements.txt
# Additional dependencies needed for testing, linting, and validating
pip3 install -r requirements-dev.txt
```

### API Keys ###

A ```keys.py``` module is required for storing API key information. Copy the following
format, replacing the placeholder text with actual keys.

```python
darksky = 'DARK_SKY_API_KEY'
adausr = 'ADAFRUIT_IO_USERNAME'
adafruit = 'ADAFRUIT_IO_API_KEY'
```

## Dependencies ##

* [darkskylib](https://github.com/lukaskubis/darkskylib) - a python library for
the [Dark Sky API](https://darksky.net/dev/docs).

* [Adafruit IO](https://github.com/adafruit/Adafruit_IO_Python) - a python
library for the
[Adafruit IO API](https://io.adafruit.com/api/docs/#adafruit-io-http-api).
See the [documentation](https://adafruit-io-python-client.readthedocs.io/en/latest/index.html)
 for more information.

* [Adafruit Seesaw](https://github.com/adafruit/Adafruit_CircuitPython_seesaw)

## I/O Components ##

* [Adafruit Soil Sensor](https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/overview)
    * Moisture reading ranges from about 200 (very dry) to 2000 (very wet). 
    * Ambient temperature from the internal temperature sensor on the microcontroller
    is not high precision, maybe good to + or - 2 degrees Celsius.

### Sensor Routing ###

GPIO # | Pi I/O | sensor I/O | JST PH Color
------ | ----- | --------- | ------------
 1 | 3V3 | VIN | Red
 3 | SDA | SDA | White
 5 | SCL | SCL | Green
 9 | GND | GND | Black

* [AM2302 (wired DHT22) temperature-humidity sensor](https://learn.adafruit.com/dht)

## General Resources ##

* [Soldering 101](https://www.instructables.com/id/Soldering-101-for-the-Beginner/)

* [Adafruit IO Basics](https://learn.adafruit.com/series/adafruit-io-basics)

* [Raspberry Pi SSH for MacOS](https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md)

* [GPIO Zero](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html)

* [Adafruit Pi GPIO Setup](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/overview)

* [Pinout](https://pinout.xyz) - an interactive overview of GPIO on the Pi.

* [FarmBot Docs](https://software.farm.bot/docs)

### Commands ###

Keeping a log of useful commands so I don't forget or have to re-look up.

Command | Descriptions | Notes
------- | ------------ | -----
```pcmanfm``` | open (pi) file system browser as root | 
```shutdown``` |... | 
```poweroff``` | ... | 
```reboot``` | ... | 
```find``` | ```sudo find [dir] -iname '*txt*'``` | 
```readlink``` | Show full file path. Use: ```readlink -f 'file'``` | 
```crontab``` | edit the Cron table, ```-e``` to edit, ```-l``` to show active. | [Pi documentation](https://www.raspberrypi.org/documentation/linux/usage/cron.md)


[version]: https://img.shields.io/badge/v-0.1.1-blue
[python-version]: https://img.shields.io/badge/python-3.7-yellow
