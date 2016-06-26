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

        a = [expandTile(tile, tile.value) for tile in options]

        m = max(a)
        maxIndexes = [i for i, j in enumerate(a) if j == m]

        return random.choice(maxIndexes)

    def expandTile(tile, current_value):
        """ given a current 'cost' and location, record the next best step """
        l =  [tile.up.value + current_value,
              tile.right.value + current_value,
              tile.left.value + current_value,
              tile.down.value + current_value]
        m = max(l)
        indices = [i for i, j in enumerate(m) if j == m]
        return random.choice(indices)

    def surroundingValues(self):
        return [self.worldMap[self.x][self.y+1],
                self.worldMap[self.x+1][self.y],
                self.worldMap[self.x][self.y-1],
                self.worldMap[self.x-1][self.y]]
