import random

class Uav:
    def __init__(x,y, worldMap):
        self.x = x
        self.y = y
        self.worldMap = worldMap
        self.sensorStrength = None

    def setMap(self, newMap):
        self.worldMap = newMap

    def nextStep(self):
        """ where should we go next tick? """
        options = self.surroundingValues()
        m = max(a)
        maxIndexes = [i for i, j in enumerate(a) if j == m]

        return random.choice(maxIndexes)

    def surroundingValues(self):
        return [self.worldMap[self.x][self.y+1],
                self.worldMap[self.x+1][self.y],
                self.worldMap[self.x][self.y-1],
                self.worldMap[self.x-1][self.y]]
