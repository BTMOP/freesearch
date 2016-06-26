import pygame
import random
from model import Grid
from view import View
from uav import Uav

pygame.init()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# initialize the map (size, num_targets)
size = 40
targets = 5
data = Grid(size,targets)

# define drones
num_drones = 10
drones = [Uav(random.randint(1,size-2), random.randint(1,size-2), data)]
for m in range(num_drones-1):
    drones.append(Uav(random.randint(1,size-2), random.randint(1,size-2), data))

# init the view of the map
view = View(600, data, drones)

# max fps at which to run
fps = 10
counter = 0

raw_input('Press <ENTER> to begin')

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): # User did something

        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    if counter == 0:
        # only update once per second (n ticks)
        for drone in drones:
            # give the drones the new map (or maybe don't) and then update
            # the map based on the drones' movement
            drone.setMap(data)
            # move 'em
            direction = drone.nextStep()

	    # 
            drone.setLocation(drone.x + direction[0], drone.y + direction[1])


            # maybe don't update map based on drone (denied comms)
            # TODO this *should* be simultaneous
            data = drone.update()

        data.update() # update the map (steps all of the diff. eqs. forward one)
        view.update(data, drones)

    counter = (counter+1) % (fps/10)

    clock.tick(fps) # max fps

pygame.quit()
