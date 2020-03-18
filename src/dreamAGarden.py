"""dreamAGarden - this module receives inputs from sensors
and decides whether or not to trigger the water pump"""

from datetime import datetime as dt
from datetime import date
from darksky import forecast
from Adafruit_IO import Client, Feed, Data
import keys
# import x from soilMonitor
# import y from temperatureHumiditySensor
# import z from waterPump

#module vars
aio = Client(keys.adausr, keys.adafruit)
dag = 'dream-a-garden.'
evl = keys.darksky, 42.2613, -78.6580
today = date.today()

def runGarden():
    feeds = aio.feeds()
    feedKeys = []
    for f in feeds:
        feedKeys.append(f.key)
        #print('Feed: {0}, key: {1}'.format(f.name,f.key))
    leKey = dag + 'last-execution'
    if leKey in feedKeys:
        lastExecution = Data(value=((dt.now()).isoformat()))
        aio.create_data(leKey, lastExecution)
        #TODO: log success
    else:
        #TODO: log error
        print('could not find LE feed')
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

def forecastFrost():
    upcomingFrost = False
    #next30Days = []
    for i in range(30):
        print(i)
        print((dt(today.year, today.month, today.day+i, 0)).isoformat())
        day = forecast(*evl, time=(dt(today.year, today.month, today.day+i, 0).isoformat()))
        #next30Days.append(day['daily']['data'][0]['temperatureLow'])
        print(day['daily']['data'][0]['temperatureLow'])
        if(day['daily']['data'][0]['temperatureLow'] < 30):
            upcomingFrost = True
    return upcomingFrost


def weatherCheck(darkskyLoc):
    print('hello')

if __name__ == '__main__':
    print('I am main')
    runGarden()
    #forecastFrost()
