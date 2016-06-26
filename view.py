import pygame
import tiles

class View:
    def __init__(self, size, grid, uavs):
        self.size = size
        h = size
        w = size
        self.squareHeight = h / grid.h # how big to make each square on the map
        self.squareWidth = w / grid.w
        self.maxH = grid.h - 1
        self.maxW = grid.w - 1
        self.screen = pygame.display.set_mode((w,h))
        pygame.display.set_caption("Alcatraz - Challenge 3")

        self.update(grid, uavs)

    def update(self, data, uavs):
        self.screen.fill((255,255,255))

        #draw tiles and targets for map
        for row in data.grid:
            for tile in row:
                rect = (tile.x * self.squareWidth,
                        tile.y * self.squareHeight,
                        self.squareWidth,
                        self.squareHeight)
                pygame.draw.rect(self.screen, tile.color(), rect, 0)
                if tile.hasTarget():
                    elip = (tile.x * self.squareWidth,
                            (tile.y * self.squareHeight)+(self.squareHeight*0.05),
                            self.squareWidth,
                            self.squareHeight*0.90)
                    pygame.draw.ellipse(self.screen, tile.targColor(), elip, 5)

        #draw drones on map
        for drone in uavs:
            circ_color = [255,162,0]
            circ_pos = ((drone.x * self.squareWidth)+(self.squareWidth/2),
                        (drone.y * self.squareHeight)+(self.squareHeight/2))
            circ_rad = min(self.squareHeight,self.squareWidth)/2
            pygame.draw.circle(self.screen, circ_color, circ_pos, circ_rad, 0) 

        # and make a screen refresh happen
        pygame.display.update()

