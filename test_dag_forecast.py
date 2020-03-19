import unittest
import dag_forecast

class dag_forecastTest(unittest.TestCase):

    mTestLat = 0.0000
    mTestLon = 0.0000
    mTestDays = 3
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
                    {'temperatureLow' : 31}
                ]
            }
        }
    }
    mTestLastFrost = {
        '2020-01-01T00:00:00' : {
            'daily' : {
                'data' : [
                    {'temperatureLow' : 29}
                ]
            }
        },
        '2020-01-02T00:00:00' : {
            'daily' : {
                'data' : [
                    {'temperatureLow' : 31}
                ]
            }
        },
        '2020-01-03T00:00:00' : {
            'daily' : {
                'data' : [
                    {'temperatureLow' : 39}
                ]
            }
        },
        '2020-01-04T00:00:00' : {
            'daily' : {
                'data' : [
                    {'temperatureLow' : 29}
                ]
            }
        },
        '2020-01-05T00:00:00' : {
            'daily' : {
                'data' : [
                    {'temperatureLow' : 36}
                ]
            }
        }
    }

    def test_retrieveForecast(self):
        validLocation = dag_forecast.retrieveForecast(self.mTestLat, self.mTestLon)
        self.assertEqual(True, validLocation != None)
        self.assertEqual(self.mTestLat, validLocation['latitude'])
        self.assertEqual(self.mTestLon, validLocation['longitude'])

    def test_retrieveForecast_badLocation(self):
        with self.assertRaises(IOError):
            dag_forecast.retrieveForecast(500.0000, -500.000)

    def test_retrieveFutureForecast(self):
        forecast = dag_forecast.retrieveFutureForecast(self.mTestLat, self.mTestLon, self.mTestDays)
        self.assertEqual(self.mTestDays, len(forecast))
    '''
    def test_retrieveFutureForecast_moreThanSixtyDays(self):
        forecast = dag_forecast.retrieveFutureForecast(self.mTestLat, self.mTestLon, 61)
        self.assertEqual(60, len(forecast))
    '''

    def test_findFirstFront(self):
        firstFrost = dag_forecast.findFirstFrost(self.mTestFistFrost)
        self.assertEqual('2020-01-04T00:00:00', firstFrost)

    def test_findLastFrost(self):
        lastFrost = dag_forecast.findLastFrost(self.mTestLastFrost)
        self.assertEqual('2020-01-04T00:00:00', lastFrost)
        