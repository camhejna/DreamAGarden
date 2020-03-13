"""dreamAGarden - this module receives inputs from sensors
and decides whether or not to trigger the water pump"""

# import x from soilMonitor
# import y from temperatureHumiditySensor
# import z from waterPump

def runGarden():
    print('running the garden')
    # initialize sensor vars
    # for each item...
    # check them,
    # and add to log file
    # decide if watering is required
    if needsWater:
        print('watering the garden')
    # send log to email/server/TBD

def needsWater():
    #check the soil sensor
    #soil status = ??
    #check the weather
    #rain in the forecast = ??
    #if soilDry and noRainSoon:
        #return True
    #else:
        #return false
    #decide
    return True

if __name__ == '__main__':
    print('I am main')
    runGarden()
