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
    daysForecast = retrieveFutureForecast(42.2613, -78.6580, 2)

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

    if daysToForecast > 60:
        mDaysToForecast = 60
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

def findFirstFrost(daysForecast):
    try:
        for date, forecast in daysForecast.items():
            if(forecast['daily']['data'][0]['temperatureLow'] <= 35):
                return date
        return
    except Exception as e:
        pass

def findLastFrost(daysForecast):
    try:
        for date in reversed(daysForecast):
            if(daysForecast[date]['daily']['data'][0]['temperatureLow'] <= 35):
                return date
        return
    except Exception as e:
        pass

if __name__ == '__main__':
    import sys
    #ffMain(float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))
    #ffMain()
    mTestFistFrost = {
        '2020-01-01T00:00:00' : {
            'daily' : {
                'data' : [
                    {'temperatureLow' : 40}
                ]
            }
        },
        '2020-01-02T00:00:00' : {
            'daily' : {
                'data' : [
                    {'temperatureLow' : 39}
                ]
            }
        },
        '2020-01-03T00:00:00' : {
            'daily' : {
                'data' : [
                    {'temperatureLow' : 41}
                ]
            }
        },
        '2020-01-04T00:00:00' : {
            'daily' : {
                'data' : [
                    {'temperatureLow' : 32}
                ]
            }
        },
        '2020-01-05T00:00:00' : {
            'daily' : {
                'data' : [
                    {'temperatureLow' : 45}
                ]
            }
        }
    }
    findLastFrost(mTestFistFrost)