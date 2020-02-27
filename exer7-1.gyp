#  Particle on a spheroid earth

""" 
This program shows the paths of particles on a spheroidal earth. The lefthand sphere is at rest in
absolute space, the right hand sphere is shown in a reference frame rotating with angular velocity w 

Code translated from GW-BASIC provided in Exercise 7.1 of Stommel and Moore (1989)

author: Victoria McDonald
email: vmcd@atmos.washington.edu
website: https://github.com/torimcd

"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class Particle(object):
    """
    Particle class. 
    Each particle travels around the spheroid in a path determined by the coriolis force.

    init_state is the initial position in lat/lon coordinates
    """

    def __init__(self):

    def position(self):

    def dstate_dt(self, state, dt):
        # compute the derivative of the given state

    def step(self, dt):
        # execute one time step of length dt and update state


# -----------------------------------------
# set up initial state and global variables

pi = 3.14159    # pi
w = 10;         # rotation rate of the earth (angular velocity) (m/s)
w2 = w^2;       
dt = 0.005;         #
fact = 60;       # scale of the display
inc = pi/16;    # inclination of the spheres  
lat = 0;        # latitude
lon = 0;        # longitude

u = 0;      # eastward velocity
v = 0;      # northward velocity


# ------------------------------------------
# set up figure and animation

fig = plt.figure()


