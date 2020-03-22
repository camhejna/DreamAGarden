"""Dream a Garden: Garden - module to handle core garden functionality.
Receives all required inputs in class constructor."""

class DAG_Garden():

    def __init__(self, weatherConditions, soilConditions, futureWeatherConditions=None):
        self.weatherConditions = weatherConditions
        self.soilConditions = soilConditions
        if futureWeatherConditions:
            self.futureWeatherConditions = futureWeatherConditions
    
    def _precipitationNotLikely(self):
        if(self.weatherConditions['precipProbability']):
            return self.weatherConditions['precipProbability'] < 0.50
        else:
            #return something else here?
            return

    def _drySoil(self):
        if(self.soilConditions['moisture']):
            return self.soilConditions['moisture'] < 350
        else:
            #return something else here?
            return

    def _coldSoil(self):
        if(self.soilConditions['temperature']):
            return self.soilConditions['temperature'] <= 36
        else:
            #return something else here?
            return

    def needsWatering(self):
        return (
            self._precipitationNotLikely and
            self._drySoil
        )

    def findFirstFrost(self):
        if(self.futureWeatherConditions):
            for date, forecast in self.futureWeatherConditions.items():
                if(forecast['temperature'] <= 35):
                    return date
            return
        else:
            raise ValueError

    def findLastFrost(self):
        if(self.futureWeatherConditions):
            for date,forecast in self.futureWeatherConditions.items():
                if(forecast['temperature'] <= 35):
                    rDate = date
                return rDate 
            return
        else:
            raise ValueError
