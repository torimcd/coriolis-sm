# Exercise 5-1: Three Surfaces of Revolution
This program shows plan view in absolute space of (1) the flat Hooke plane, (2) the paraboloid of revolution, (3) the hemisphere, concave up, from left to right.
Below them there are also shown a vertical section through each surface.

Code translated from GW-BASIC provided in Exercise 5.1 of Stommel and Moore (1989)

""" 
author: Victoria McDonald
email: vmcd@atmos.washington.edu
website: https://github.com/torimcd/coriolis-sm

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import random
from IPython.display import HTML
%matplotlib inline


This function returns a random number between 1 and 0. In the python code files in the repository is is contained in the coriolis_tools module and is reused in multiple exercises.

def rnd():
    ''' Helper function returns a random number between 0 and 1 '''
    rand = random.uniform(0,1)
    return rand

Here we set up initial values for the constants, and initialize the objects holding the variables that change on each step of the animation.

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

The following code sets up the figure and empty plot object for the position of the particle. The x, y values are updated and set in the update() function for each step of the animation.

%%capture

# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(-100, 100), ax.set_xticks([])
ax.set_ylim(-100, 100), ax.set_yticks([])

# Construct the plot which we will update during animation
# as the particle moves.
pos, = ax.plot([], [], 'ro', ms=2, animated=True)


This is the update function that calculates the new position of the particle depending on whether the force is turned on or not

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
        ax.add_patch(patches.Arrow(arrow_x, arrow_y, arrow_dx, arrow_dy, facecolor='gold', width=4, visible=True))
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

This init() function initializes the animation and resets the plot when the animation repeats when run in the python code file. Here only one run of the animation is visible through the embedded player below. If you download the python code files in the repository the animation repeats with new random values for the particle's initial trajectory and the magnitude of the force. 

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
    dxdt = trajectory_scale_factor*(rnd()-0.5)
    dydt = trajectory_scale_factor*(rnd()-0.5)
    d2xdt2 = 0
    d2ydt2 = 0

    # initialize the force that will act on the particle
    force_x_direction = force_scale_factor*(rnd()-0.5)
    force_y_direction = force_scale_factor*(rnd()-0.5)

    # initializa the arrow indicating hte strength and direction of the force on the particles
    arrow_x = 10
    arrow_y = -10
    arrow_dx = arrow_scale_factor*force_x_direction
    arrow_dy = arrow_scale_factor*force_y_direction

    pos.set_data([], [])
    return pos


Here we construct the animation and embed an animation of a single run in this webpage. If you download this Jupyter Notebook file, or the python code files from the repository, each time you run the below code a different trajectory and force will be applied. 

# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, update, init_func=init, frames=n-1, interval=300, repeat=True, blit=False)
# convert to a video to be embedded in web page
HTML(animation.to_jshtml())