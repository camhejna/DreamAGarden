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

def ffMain():
    #daysForecast = retrieveFutureForecast(42.2613, -78.6580, 2)
    pass

def retrieveForecast(latitude, longitude):
    '''Returns a Dark Sky Forecast Request for the given coordinates.
    Throws an IOError.'''

    try:
        return forecast(mDSK, latitude, longitude)
    except IOError as e:
        raise e

def retrieveFutureForecast(latitude, longitude, daysToForecast):
    '''Returns a Dark Sky Time Machine Request for the given latitude,
    longitude and for the number of days to forecast up to 60
    (Dark Sky Time Machine maximum).'''

    if daysToForecast > mTimeMachineMax:
        mDaysToForecast = mTimeMachineMax
    else:
        mDaysToForecast = daysToForecast
    today = dt.today()
    location = mDSK, latitude, longitude
    daysForecast = {}
    for i in range(mDaysToForecast):
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

def _findFirstFrost(daysForecast):
    try:
        for date, forecast in daysForecast.items():
            if(forecast['daily']['data'][0]['temperatureMin'] <= 35):
                return date
        return
    except Exception as e:
        raise e

def findFirstFrost(latitude, longitude):
    '''Given a latitude and longitude, return the first frost date
    for the next 10 days, or none if there is no frost in that range'''
    return _findFirstFrost(retrieveFutureForecast(latitude, longitude, mTimeMachineMax))

def _findLastFrost(daysForecast):
    try:
        for date in reversed(daysForecast.keys()):
            if(daysForecast[date]['daily']['data'][0]['temperatureMin'] <= 35):
                return date
        return
    except Exception as e:
        raise e

def findLastFrost(latitude, longitude):
    '''Given a latitude and longitude, returns the last frost date
    for the next 10 days, or none is there is no frost in that range.'''
    return _findLastFrost(retrieveFutureForecast(latitude, longitude, mTimeMachineMax))

if __name__ == '__main__':
    import sys
    lf = findLastFrost(47.0000, -78.0000)
    print(lf)