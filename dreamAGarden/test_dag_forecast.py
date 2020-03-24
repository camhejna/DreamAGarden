import unittest
from dag_forecast import DAG_Forecast

class dag_forecastTest(unittest.TestCase):

    mTestLat = 0.0000
    mTestLon = 0.0000
    mTestDays = 3
    """
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
    """

    def setup(self) -> None:
        self.df = DAG_Forecast(self.mTestLat, self.mTestLon)

    def tearDown(self) -> None:
        pass

    def test_retrieveForecast(self):
        validLocation = self.df.retrieveForecast()
        self.assertEqual(True, validLocation != None)
        self.assertEqual(self.mTestLat, validLocation['latitude'])
        self.assertEqual(self.mTestLon, validLocation['longitude'])

    def test_retrieveForecast_badLocation(self):
        with self.assertRaises(IOError):
            df = DAG_Forecast(500.000, -5000.000)
            df.retrieveForecast()

    def test_retrieveFutureForecast(self):
        forecast = self.df.retrieveFutureForecast(daysToForecast=self.mTestDays)
        self.assertEqual(self.mTestDays, len(forecast))
    
    @unittest.skip('LargeAPI')
    def test_retrieveFutureForecast_moreThanSixtyDays(self):
        forecast = self.df.retrieveFutureForecast(11)
        self.assertEqual(10, len(forecast))
