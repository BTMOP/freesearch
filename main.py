import pygame
import time
from model import Grid
from view import View

pygame.init()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# initialize the map (size, num_targets)
data = Grid(100,50)

# init the view of the map
view = View(600, data)

# temporary
# TODO need to fix the data.update() for UAV movement
# remove this when fixed
time.sleep(10000)

# max fps at which to run
fps = 10
counter = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): # User did something

        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    if counter == 0:
        # only update once per second (n ticks)
        data.update() # update the map (steps all of the diff. eqs. forward one)
        view.update(data)

    counter = (counter+1) % (fps/10)

    clock.tick(fps) # max fps

pygame.quit()
