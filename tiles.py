import random

import math
import numpy as np

class bordertile(object):
    '''dummy class for border tiles. gets rid of edge cases.'''
    def __init__(self, loc):
        self.x = loc[0]
        self.y = loc[1]
        self.isedge = True
        self.explored = 0
        self.hasTarg = False

    def color(self):
        return [0, 0, 0]

class tile(object):
    '''class for tiles on the map. each tile has a population. sometimes it is water'''
    def __init__(self, targ, loc):
        '''initializes each tile with a location, a population, and a water state'''
        self.x = loc[0]
        self.y = loc[1]
        self.isedge = False
        self.explored = 0
        self.hasTarg = targ

    def setTarget(self, targ):
        self.hasTarg = targ

    def hasTarget(self):
        return self.hasTarg

    def update(self):
        '''spits out a new population one time step in the future'''
        return

    def findneighbors(self,tilegrid):
        '''once the entire grid is populated with tiles, find the neighbors'''
        self.left = tilegrid[self.x-1][self.y]
        self.up = tilegrid[self.x][self.y-1]
        self.down = tilegrid[self.x][self.y+1]
        self.right = tilegrid[self.x+1][self.y]
        horiz = [self.left.isedge, self.right.isedge]
        vert = [self.up.isedge, self.down.isedge]
        #lowpass filter
        if horiz == [True, True] or vert == [True, True]:
            if self.isedge == False:
                self.isedge = True
        if horiz == [False, False] or vert == [False, False]:
            if self.isedge == True:
                self.isedge == False

    def color(self):
        '''generate a color for the tile. to be used in pygame'''
        if self.hasTarg:
            return [255, 0, 0]
        elif not self.isedge:
            return [0,0,255]
        else:
            return [105,105,105]
