import random

class Uav:
    def __init__(self, x, y, worldMap):
        self.x = x
        self.y = y
        self.worldMap = worldMap
        self.sensorStrength = .5
        self.speed = 1
        self.altitude = 1

    def setMap(self, newMap):
        self.worldMap = newMap

    def setLocation(self, x, y):
        self.x = x
        self.y = y

    def nextStep(self):
        """ where should we go next tick? """
        options = self.surroundingValues()

        a = [self.expandTile(tile, tile.explored) for tile in options]

        m = max(a)
        maxIndexes = [i for i, j in enumerate(a) if j == m]

        direction = random.choice(maxIndexes)

        # go from index in the array to an actual direction
        if direction == 0:
            return [0,1]
        elif direction == 1:
            return [1,0]
        elif direction == 2:
            return [0,-1]
        elif direction == 3:
            return [-1,0]

        raise ValueError('wat')
        return

    def expandTile(self, tile, current_value):
        """ given a current 'cost' and location, record the next best step """
        if tile.isedge == True:
            return False
        adjacent = [tile.up, tile.right, tile.down, tile.left]
        l =  [tile.up.explored + current_value,
              tile.right.explored + current_value,
              tile.down.explored + current_value,
              tile.left.explored + current_value]
        m = max(l)
        indices = [i for i, j in enumerate(l) if j == m]
        return random.choice(indices)

    def surroundingValues(self):
        return [self.worldMap.grid[self.x][self.y+1],
                self.worldMap.grid[self.x+1][self.y],
                self.worldMap.grid[self.x][self.y-1],
                self.worldMap.grid[self.x-1][self.y]]

    def explore(self, tile):
        """ given a tile, calculate and return a delta value of the exploration value for it """
        currentVal = tile.explored
        multiplier = self.sensorStrength / (self.speed * self.altitude)
        delta = multiplier * (1 - currentVal)
        return delta

    def update(self):
        currentTile = self.worldMap.grid[self.x][self.y]
        currentTile.explored += self.explore(currentTile)
        return self.worldMap
