import busio
from board import SCL, SDA
from adafruit_seesaw.seesaw import Seesaw

#TODO: change busing based on IRL wiring
i2c_bus = busio.I2C(SCL, SDA) #this is based on example data, not actual config

ss = Seesaw(i2c_bus, addr=0x36)

def readSensor():
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read() * 9/5 + 32

    # read temperature from the temperature sensor
    temp = ss.get_temp()

    retval = {'touch':touch, 'temp':temp}
    return retval

if __name__ == '__main__':
    sense = readSensor()
    print(('temp: {0}, moisture: {1}').format(
        sense['temp'],
        sense['touch']
    ))
    