from dreamAGarden import Garden

latitude = 42.9046
longitude = -78.8708
location = 'Buffalo'

if __name__ == 'main':
    garden = Garden(latitude, longitude, location)
    garden.runGarden()
