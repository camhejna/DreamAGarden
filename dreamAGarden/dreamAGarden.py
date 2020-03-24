'''dreamAGarden - this module receives inputs from sensors
and decides whether or not to trigger the water pump'''

from datetime import datetime as dt
from datetime import date
from darksky import forecast
from Adafruit_IO import Client, Feed, Data
from soilMonitor import readSensor
# import y from temperatureHumiditySensor
# import z from waterPump
import dag_adafruit
from dag_forecast import DAG_Forecast
from dag_garden import DAG_Garden

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
        self.forecast = DAG_Forecast(self._parameters['latitude'],self._parameters['longitude'])
        self.soilConditions = readSensor()
        self.feedKeys = {}
        for f in dag_adafruit.getFeeds():
            self.feedKeys[f.name] = f.key

    def _logLastExecution(self):
        """Logs the last execution of this method to the relevant
        Adafruit IO feed."""
        if self.feedKeys['Last Execution']:
            lastExecution = Data(value=((dt.now()).isoformat(timespec='seconds')))
            dag_adafruit.createData(self.feedKeys['Last Execution'], lastExecution)

    def _logSoilConditions(self):
        """Logs the soil temperature and moisture data from the 
        sensor to the relevant Adafruit IO feeds."""
        if self.feedKeys['Soil Temperature']:
            st = Data(value=str(self.soilConditions['temp']))
            dag_adafruit.createData(self.feedKeys['Soil Temperature'], st)
        if self.feedKeys['Soil Moisture']:
            sm = Data(value=str(self.soilConditions['touch']))
            dag_adafruit.createData(self.feedKeys['Soil Moisture'], sm)

    def runGarden(self):
        """runs through all the components of the garden and
        decides whether or not to water the garden."""
        # initialize sensor vars
        #TODO: Sensors
        weatherConditions = {
            'precipProbability':self.forecast.dailyPrecipProbability
        }
        soilConditions = self.soilConditions
        fwc = self.forecast.retrieveFutureForecast
        g = DAG_Garden(
            weatherConditions,
            soilConditions,
            futureWeatherConditions=fwc
        )
        if g.needsWatering():
            print('watering the garden')
        # send log to email/server/TBD

        # FOR TESTING IN DEVELOPMENT
        print(('First frost: {0}').format(self.findFirstFrost(g)))
        print(('Last frost: {0}').format(self.findLastFrost(g)))

        # Log results
        self._logLastExecution()
        self._logSoilConditions()
        print('\nEnd of Garden\n\n\n----------------------------------------------------------\n\n')

    def needsWater(self):
        if self.forecast.dailyPrecipProbability > 0.50:
            return False
        else:
            return True

    def findFirstFrost(self, garden):
        firstFrost = garden.findFirstFrost()
        if self.feedKeys['First Frost'] and firstFrost:
            logFirstFrost = ('location":{0},"latitude":{1},"longitude":{2},"frostDate":{3}').format(
                self._parameters['location'],
                self._parameters['latitude'],
                self._parameters['longitude'],
                firstFrost)
            logFirstFrost = '{'+logFirstFrost+'}'
            lfData=Data(value=logFirstFrost)
            dag_adafruit.createData(self.feedKeys['First Frost'], lfData)
        return firstFrost

    def findLastFrost(self, garden):
        lastFrost = garden.findLastFrost()
        if self.feedKeys['Last Frost'] and lastFrost:
            logLastFrost = ('location":{0},"latitude":{1},"longitude":{2},"frostDate":{3}').format(
                self._parameters['location'],
                self._parameters['latitude'],
                self._parameters['longitude'],
                lastFrost)
            logLastFrost = '{'+logLastFrost+'}'
            lfData=Data(value=logLastFrost)
            dag_adafruit.createData(self.feedKeys['Last Frost'], lfData)
        return lastFrost

if __name__ == '__main__':
    import sys
    garden = Garden(float(sys.argv[1]), float(sys.argv[2]), str(sys.argv[3]))
    garden.runGarden()
