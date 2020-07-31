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
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from coriolis_tools import tools

# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(-100, 100), ax.set_xticks([])
ax.set_ylim(-100, 100), ax.set_yticks([])

# set constants
force_scale_factor = 10
arrow_scale_factor = 10
trajectory_scale_factor = 10

# x and y need to be lists so we can clear the frame when the animation repeats
x = []
y = []
dxdt = 0
dydt = 0
d2xdt2 = 0
d2ydt2 = 0

force_x_direction = 0
force_y_direction = 0

arrow_x = 0
arrow_y = 0
arrow_dx = 0
arrow_dy = 0

# Construct the plot which we will update during animation
# as the particle moves.
pos, = ax.plot([], [], 'ro', ms=2)

# number of frames in each animation
n=20

# function to update the animation frame with the particle's new position
def update(frame):
    # ensure we're using the same variables throughout
    global x
    global y
    global dxdt
    global dydt
    global d2xdt2
    global d2ydt2

    # force on the particel is zero for first 10 steps
    if frame < 9:
        force_x = 0
        force_y = 0
    else:
        # after 10 steps turn the force on
        ax.add_patch(patches.Arrow(arrow_x, arrow_y, arrow_dx, arrow_dy, color='y', width=2, visible=True))
        force_x = force_x_direction
        force_y = force_y_direction

    # update the acceleration of the particle
    d2xdt2 = force_x
    d2ydt2 = force_y

    # update the velocity of the particle
    dxdt = d2xdt2 + dxdt
    dydt = d2ydt2 + dydt

    # update the position of the particle
    x.append(dxdt + x[frame])
    y.append(dydt + y[frame])

    # update the animation
    pos.set_data(x[-n:], y[-n:])

    return pos

def init():
    global x
    global y
    global dxdt
    global dydt
    global d2xdt2
    global d2ydt2
    global force_scale_factor
    global force_x_direction
    global force_y_direction
    global arrow_x
    global arrow_y
    global arrow_dx
    global arrow_dy

    # remove previous particles if they exist
    x[:] = []
    y[:] = []
    # remove previous arrow if it exists
    ax.patches = []

    # Initialize the particles at 0,0 with random velocity
    x.append(0)
    y.append(0)
    dxdt = trajectory_scale_factor*(tools.rnd()-0.5)
    dydt = trajectory_scale_factor*(tools.rnd()-0.5)
    d2xdt2 = 0
    d2ydt2 = 0

    # initialize the force that will act on the particle
    force_x_direction = force_scale_factor*(tools.rnd()-0.5)
    force_y_direction = force_scale_factor*(tools.rnd()-0.5)

    # initializa the arrow indicating hte strength and direction of the force on the particles
    arrow_x = 10
    arrow_y = -10
    arrow_dx = arrow_scale_factor*force_x_direction
    arrow_dy = arrow_scale_factor*force_y_direction

    pos.set_data([], [])
    return pos

# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, update, init_func=init, frames=n-1, interval=300, repeat=True, blit=False)
plt.show()