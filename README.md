# **Dream A Garden** #

![version]

another IOT Garden

## Dependencies ##

[darkskylib](https://github.com/lukaskubis/darkskylib) - a python library for the [Dark Sky API](https://darksky.net/dev/docs).
[Adafruit IO](https://github.com/adafruit/Adafruit_IO_Python) - a python library for the Adafruit IO API. All feeds are part of the default group, but are prefixed with 'dag_'. This is because, during early development, I continually received 404 errors when trying to access feeds in a different group. I did not have this issue when using feeds only in the default group.

## I/O Components ##

[Adafruit Soil Sensor](https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/overview)

[AM2302 (wired DHT22) temperature-humidity sensor](https://learn.adafruit.com/dht)

[version]: https://img.shields.io/badge/v-0.1-blue
