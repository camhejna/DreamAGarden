'''Dream A Garden: Adafruit - module to handler API calls to 
Adafruit IO API calls'''

from Adafruit_IO import Client, Feed, Data
import keys

mAIO = Client(keys.adausr, keys.adafruit)

def createData(feed, data):
    mAIO.create_data(feed, data)

if __name__ == '__main__':
    print('This module is not built to be run standalone')