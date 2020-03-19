'''Dream A Garden: Forecast - module to handle all API calls to the
DarkSky API'''

from datetime import datetime as dt
from datetime import timedelta
from datetime import date
from darksky import forecast
import keys

mDSK = keys.darksky
mDaysToForecast = 60

def ffMain():
    daysForecast = retrieveFutureForecast(42.2613, -78.6580, 60)

def retrieveForecast(latitude, longitude):
    return forecast(mDSK, latitude, longitude)

def retrieveFutureForecast(latitude, longitude, daysToForecast):
    '''makes a time machine API request for the given latitude,
    longitude and for the number of days to forecast up to 60
    (Dark Sky Time Machine maximum).'''

    if daysToForecast > 60:
        mDaysToForecast = 60
    else:
        mDaysToForecast = daysToForecast
    today = date.today()
    location = mDSK, latitude, longitude
    daysForecast = {}
    for i in range(mDaysToForecast):
        dateF = today + timedelta(days=i)
        try:
            frost = forecast(*location, time=dateF.isoformat())
            daysForecast[dateF] = frost
        except Exception as e:
            #throw exception for bad values (lat/long)
            raise ValueError
        finally:
            pass
    return daysForecast

def findFirstFrost(daysForecast):
    try:
        for date, forecast in daysForecast.items():
            if(forecast['daily']['data'][0]['temperatureLow'] <= 35):
                firstFrost = date
                return firstFrost
        return
    except Exception as e:
        pass

def findLastFrost(daysForecast):
    try:
        for date in reversed(daysForecast):
            if(daysForecast[date]['daily']['data'][0]['temperatureLow'] <= 35):
                lastFrost = date
                return lastFrost
        return
    except Exception as e:
        pass

if __name__ == '__main__':
    import sys
    #ffMain(float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))
    ffMain()