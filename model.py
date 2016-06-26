from tiles import tile, bordertile
import numpy as np
from random import randint
import math
from copy import copy, deepcopy

class Grid:
    def __init__(self, size, num_targ):
        # create the map
        self.h = size
        self.w = size
        self.grid = [[0 for x in range(self.w)] for y in range(self.h)]
        # populate the edges
        for x in range (self.w):
            loc = [x, 0]
            self.grid[x][0] = bordertile(loc)
            loc = [x, self.h-1]
            self.grid[x][self.h-1] = bordertile(loc)
        for y in range (self.h):
            loc = [0, y]
            self.grid[0][y] = bordertile(loc)
            loc = [self.w-1, y]
            self.grid[self.w-1][y] = bordertile(loc)
        # fill it with tile objects
        for y in range(1, self.h-1):
            for x in range(1, self.w-1):
                loc = [x,y]
                self.grid[x][y] = tile(False,loc)
        # fill tiles with targets
        for m in range(num_targ):
            loc = [randint(1,self.w-1),randint(1,self.h-1)]
            while self.grid[loc[0]][loc[1]].hasTarget():
                loc = [randint(1,self.w-1),randint(1,self.h-1)]
            self.grid[loc[0]][loc[1]].setTarget(True)
        #get neighbors of tiles
        for m in range(2):
            for y in range(1, self.h-1):
                for x in range(1, self.w-1):
                    self.grid[x][y].findneighbors(self.grid)

    def update(self):
        ''' advance the DEs by one tick '''
        for y in range(1, self.h-1):
            for x in range(1, self.w-1):
                self.grid[x][y].popout()
                self.grid[x][y].update()
        return
