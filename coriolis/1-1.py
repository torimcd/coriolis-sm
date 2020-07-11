#  Particle accelerating under suddenly turned-on force

""" 
This program shows the paths of particles starting at the origin and travelling in a random direction. After 10 timesteps a force with a random 
magnitude turns on and the particle accelerates in the direction of the force. The force magnitude and direction is shown by an arrow centered at the origin.

Code translated from GW-BASIC provided in Exercise 1.1 of Stommel and Moore (1989)

author: Victoria McDonald
email: vmcd@atmos.washington.edu
website: https://github.com/torimcd/coriolis-sm

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from coriolis_tools import tools

# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(-100, 100), ax.set_xticks([])
ax.set_ylim(-100, 100), ax.set_yticks([])

# Create particle
particle = {}

# Initialize the particles at 0,0 with random velocity
particle['position'] = (0, 0)
particle['velocity'] = (tools.rnd()-0.5, tools.rnd()-0.5)
particle['force'] =  (0, 0)
particle['curve'] = (0, 0)

force_x_direction = (tools.rnd()-0.5)
force_y_direction = (tools.rnd()-0.5)

arrow_x = 1
arrow_y = -1
arrow_dx = arrow_x + force_x_direction
arrow_dy = arrow_y + force_y_direction

# Construct the scatter which we will update during animation
# as the raindrops develop.
pos, = ax.plot([], [], 'ro')
#arrow = ax.arrow(arrow_x, arrow_y, arrow_dx, arrow_dy, color='y', width=0.05, shape='full', visible=True)

def update(frame):
    arrow = ax.arrow(arrow_x, arrow_y, arrow_dx, arrow_dy, color='y', width=0.05, shape='full', visible=True)
    if frame < 10:
        force_x = 0
        force_y = 0
        arrow.remove()
    else:
        force_x = force_x_direction
        force_y = force_y_direction

    print(frame)
    particle['curve'] = (force_x, force_y)

    particle['velocity'] = (particle['curve'][0]*frame + particle['velocity'][0], particle['curve'][1]*frame + particle['velocity'][1])

    particle['position'] = (particle['velocity'][0]*frame + particle['position'][0], particle['velocity'][1]*frame + particle['position'][1])

    pos.set_data(particle['position'][0], particle['position'][1])

def init():
    pos.set_data([], [])

# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, update, init_func=init, frames=20, interval=500, repeat=False, blit=False)
plt.show()