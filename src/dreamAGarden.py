"""dreamAGarden - this module receives inputs from sensors
and decides whether or not to trigger the water pump"""

# import x from soilMonitor
# import y from temperatureHumiditySensor
# import z from waterPump
from datetime import datetime as dt
from darksky import forecast
import keys

def runGarden():
    print('running the garden')
    # initialize sensor vars
    # for each item...
    # check them,
    # and add to log file
    # decide if watering is required
    if needsWater():
        print('watering the garden')
    # send log to email/server/TBD

def needsWater():
    print('checking the weather')
    evl = keys.darksky, 42.2613, -78.6580
    evlNow = forecast(*evl)
    print(evlNow['currently']['precipProbability'])
    retVal = False
    try:
        retVal = (evlNow['currently']['precipProbability'] > 0.3)
    except TypeError as te:
        print('typeError')
        print(te)
        #log te
    finally:
        return retVal 
    #check the soil sensor
    #soil status = ??
    #check the weather
    #rain in the forecast = ??
    #if soilDry and noRainSoon:
        #return True
    #else:
        #return false
    #decide
    #return True

def weatherCheck(darkskyLoc):
    print('hello')

if __name__ == '__main__':
    print('I am main')
    runGarden()
