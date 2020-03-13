def runGarden():
    print('running the garden')
    # initialize sensor vars
    # for each item...
    # check them,
    # and add to log file
    # decide if watering is required
    if needsWater:
        print('watering the garden')
    # send log to email/server/TBD

def needsWater():
    return True

if __name__ == '__main__':
    print('I am main')
    runGarden()
