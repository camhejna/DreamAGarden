'''Dream A Garden: Adafruit - module to handler API calls to 
Adafruit IO API calls'''

from Adafruit_IO import Client, Feed, Data
import keys

mAIO = Client(keys.adausr, keys.adafruit)

def sendData(feed, data):
    try:
        mAIO.create_data(feed, data)
    except Exception as e:
        raise e

def getFeeds():
    return mAIO.feeds()

if __name__ == '__main__':
    print('This module is not built to be run standalone')