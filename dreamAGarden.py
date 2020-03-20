'''dreamAGarden - this module receives inputs from sensors
and decides whether or not to trigger the water pump'''

from datetime import datetime as dt
from datetime import date
from darksky import forecast
from Adafruit_IO import Client, Feed, Data
#from soilMonitor import readSensor
# import y from temperatureHumiditySensor
# import z from waterPump
import dag_adafruit
import dag_forecast
import keys

#module vars
#aio = Client(keys.adausr, keys.adafruit)
#dag = 'dream-a-garden.'
#evl = keys.darksky, 42.2613, -78.6580
#today = date.today()

class Garden():

    def __init__(self, latitude, longitude, location='N/A'): 
        #TODO:fix inconsistency in class vars here
        self._parameters = dict(latitude=latitude, longitude=longitude, location=location)
        self.feedKeys = {}
        for f in dag_adafruit.getFeeds():
            self.feedKeys[f.name] = f.key
        self.logLastExecution()

    def logLastExecution(self):
        """Logs the last execution of this method to the relevant
        Adafruit IO feed."""
        if self.feedKeys['Last Execution']:
            lastExecution = Data(value=((dt.now()).isoformat(timespec='seconds')))
            dag_adafruit.sendData(self.feedKeys['Last Execution'], lastExecution)

    def runGarden(self):
        """runs through all the components of the garden and
        decides whether or not to water the garden."""
        
        feeds = dag_adafruit.getFeeds()
        feedKeys = []
        for f in feeds:
            feedKeys.append(f.key)
            #print('Feed: {0}, key: {1}'.format(f.name,f.key))
        #leKey = self.dag + 'last-execution'
        #if leKey in feedKeys:
        #    lastExecution = Data(value=((dt.now()).isoformat()))
        #    dag_adafruit.sendData(leKey, lastExecution)
            #TODO: log success
        #else:
            #TODO: log error
        #    print('could not find LE feed')
        print('running the garden')
        # initialize sensor vars
        # for each item...
        # check them,
        
        # and add to log file
        # decide if watering is required
        if self.needsWater():
            print('watering the garden')
        # send log to email/server/TBD

    def needsWater(self):
        pass

    def logLastFrost(self):
        if self.feedKeys['Last Frost']:
            lastFrost = dag_forecast.findLastFrost(
                self._parameters['latitude'],
                self._parameters['longitude'])
            logLastFrost = ('location":{0},"latitude":{1},"longitude":{2},"frostDate":{3}').format(
                self._parameters['location'],
                self._parameters['latitude'],
                self._parameters['longitude'],
                lastFrost)
            logLastFrost = '{'+logLastFrost+'}'
            print(logLastFrost)
            lfData=Data(value=logLastFrost)
            dag_adafruit.sendData(self.feedKeys['Last Frost'], lfData)
        

if __name__ == '__main__':
    import sys
    garden = Garden(float(sys.argv[1]), float(sys.argv[2]), str(sys.argv[3]))
    #print(garden)
    garden.logLastFrost()
    #forecastFrost()
