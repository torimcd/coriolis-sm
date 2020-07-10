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
from matplotlib import animation
from coriolis_tools import tools


FAC = 10
FFF = 10
FFC = 10
CA = 3

time = 0 # initial time is 0
dt = 1  # timestep increass by 1

# set the initial position of the particle at the origin
x=0
y=0

# set random initial values for dx and dy
dxdt = FFC*(tools.rnd()-0.5)
dydt = FFC*(tools.rnd()-0.5)

force_x_direction = FFF*(tools.rnd()-0.5)
force_y_direction = FFF*(tools.rnd()-0.5)


def update_particle_position(frame, x, y, force_x, force_y, time):
    '''
    Function to return the next particle position given the current position, current forcing, and time step
    -----------
    Parameters:
    x: the current x position of the particle
    y: the current y position of the particle
    force_x: the foring in the x-direction
    force_y: the forcing in the y-direction
    time: the current time step
    --------
    Returns: the next x and y position
    '''

    if time < (11*dt):
        force_x = 0
        force_y = 0
    else:
        force_x = force_x_direction
        force_y = force_y_direction

    # initial values for the second derivatives
    d2xdt2 = force_x
    d2ydt2 = force_y

    # here are the equations of motion
    dxdt = d2xdt2*dt + dxdt
    dydt = d2ydt2*dt + dydt

    x = dxdt*dt + x
    y = dydt*dt + y

    time = time + dt

    return (x, y)


fig = plt.figure()
ax = fig. add_subplot(111, aspect='equal', xlim=(-10, 10), ylim=(-10,10))

if x^2 + y^2 > 10000:
    restart()
