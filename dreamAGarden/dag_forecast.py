'''Dream A Garden: Forecast - module to handle all API calls to the
DarkSky API'''

from datetime import datetime as dt
from datetime import timedelta
from datetime import date
from darksky import forecast
import keys

mDSK = keys.darksky
mDaysToForecast = 10
mTimeMachineMax = 10

class DAG_Forecast():

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.key = keys.darksky
        self.timeMachineMax = 10

    def retrieveForecast(self):
        """Returns a Dark Sky Forecast Request for the given coordinates.
        Throws an IOError."""
        try:
            return forecast(self.key, self.latitude, self.longitude)
        except IOError as e:
            raise e

    def retrieveFutureForecast(self, daysToForecast=10):
        """Returns a Dark Sky Time Machine Request for the given latitude,
        longitude and for the number of days to forecast up to 10
        (Dark Sky Time Machine maximum).
        :param int daysToForecast: number of days to forecast. Integers greater than 10 will be set to 10."""
        if daysToForecast > self.timeMachineMax:
            daysToForecast = mTimeMachineMax
        today = dt.today()
        location = self.key, self.latitude, self.longitude
        daysForecast = {}
        for i in range(daysToForecast):
            dateF = (today + timedelta(days=i)).isoformat(timespec='seconds')
            try:
                frost = forecast(*location, time=dateF)
                daysForecast[dateF] = frost
            except Exception as e:
                #throw exception for bad values (lat/long)
                raise e
            finally:
                pass
        return daysForecast

    def dailyPrecipProbability(self):
        """Returns a float of the probability of precipitation for today at the
        instance coordinates."""
        return self.retrieveForecast()['daily']['data'][0]['precipProbability']

if __name__ == '__main__':
    import sys
