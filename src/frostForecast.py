"""frostForecast - because frost forecasting requires a large number
of API calls to darksky, this needs to be run seperately from 
dreamAGarden.runGarden().
"""

from datetime import datetime as dt
from datetime import timedelta
from datetime import date
from darksky import forecast
import keys

mDaysToForecast = 60

def ffMain():
    daysForecast = retrieveFutureForecast(42.2613, -78.6580, 60)

def retrieveFutureForecast(latitude, longitude, daysToForecast):
    if daysToForecast > 60:
        mDaysToForecast = 60
    else:
        mDaysToForecast = daysToForecast
    today = date.today()
    location = keys.darksky, latitude, longitude
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
        #print(i)
        #print((dt(today.year, today.month, today.day+i, 0)).isoformat())
        #day = forecast(*location, time=(dt(today.year, today.month, today.day+i, 0).isoformat()))
        #next30Days.append(day['daily']['data'][0]['temperatureLow'])
        #print(day['daily']['data'][0]['temperatureLow'])
        #if(day['daily']['data'][0]['temperatureLow'] < 30):
        #    upcomingFrost = True
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
    ffMain()