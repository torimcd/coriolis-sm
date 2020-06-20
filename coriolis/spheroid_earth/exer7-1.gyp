#  Particle on a spheroid earth

""" 
This program shows the paths of particles on a spheroidal earth. The lefthand sphere is at rest in
absolute space, the right hand sphere is shown in a reference frame rotating with angular velocity w 

Code translated from GW-BASIC provided in Exercise 7.1 of Stommel and Moore (1989)

author: Victoria McDonald
email: vmcd@atmos.washington.edu
website: https://github.com/torimcd

"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import numpy as np

""" class Particle(object):
  """  """
    Particle class. 
    Each particle travels around the spheroid in a path determined by the coriolis force.

    init_state is the initial position in lat/lon coordinates
    """
"""
    def __init__(self):

    def position(self):

    def dstate_dt(self, state, dt):
        # compute the derivative of the given state

    def step(self, dt):
        # execute one time step of length dt and update state
 """



# -----------------------------------------
# set up initial state and global variables

pi = np.pi    # pi
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

ax_fixed = fig.add_subplot(121, aspect='auto')

# create oblate spheroids out of ellipse patches for outline and lats
fixed_outline = patches.Ellipse((0,0), 12, 10, 0, linewidth=2, fill=False)
fixed_center_lat = patches.Ellipse((0,0), 12, 10*np.sin(inc), 0, linewidth=1, fill=False)

c9 = 5*np.sin(pi/6)*np.cos(inc)
c8 = 5*np.sin(pi/3)*np.cos(inc)

fixed_mid_lat_up = patches.Ellipse((0,0+c9), 12*np.cos(pi/6), 7.5*np.sin(inc), 0, linewidth=1, fill=False)
fixed_mid_lat_down = patches.Ellipse((0,0-c9), 12*np.cos(pi/6), 7.5*np.sin(inc), 0, linewidth=1, fill=False)
fixed_pole_lat_up = patches.Ellipse((0,0+c8), 12*np.cos(pi/3), 5*np.sin(inc), 0, linewidth=1, fill=False)
fixed_pole_lat_down = patches.Ellipse((0,0-c8), 12*np.cos(pi/3), 5*np.sin(inc), 0, linewidth=1, fill=False)

# add the ellipses to the plot
ax_fixed.add_patch(fixed_outline)
ax_fixed.add_patch(fixed_center_lat)
ax_fixed.add_patch(fixed_mid_lat_up)
ax_fixed.add_patch(fixed_mid_lat_down)
ax_fixed.add_patch(fixed_pole_lat_up)
ax_fixed.add_patch(fixed_pole_lat_down)
ax_fixed.set_aspect('equal')

# Turn off axes
plt.axis('off')


ax_rot = fig.add_subplot(122, aspect='auto')
# create ellipse patches for outline and lats
rot_outline = patches.Ellipse((0,0), 12, 10, 0, linewidth=2, fill=False)
rot_center_lat = patches.Ellipse((0,0), 12, 10*np.sin(inc), 0, linewidth=1, fill=False)

rot_mid_lat_up = patches.Ellipse((0,0+c9), 12*np.cos(pi/6), 7.5*np.sin(inc), 0, linewidth=1, fill=False)
rot_mid_lat_down = patches.Ellipse((0,0-c9), 12*np.cos(pi/6), 7.5*np.sin(inc), 0, linewidth=1, fill=False)
rot_pole_lat_up = patches.Ellipse((0,0+c8), 12*np.cos(pi/3), 5*np.sin(inc), 0, linewidth=1, fill=False)
rot_pole_lat_down = patches.Ellipse((0,0-c8), 12*np.cos(pi/3), 5*np.sin(inc), 0, linewidth=1, fill=False)

# add the ellipses to the plot
ax_rot.add_patch(rot_outline)
ax_rot.add_patch(rot_center_lat)
ax_rot.add_patch(rot_mid_lat_up)
ax_rot.add_patch(rot_mid_lat_down)
ax_rot.add_patch(rot_pole_lat_up)
ax_rot.add_patch(rot_pole_lat_down)

ax_rot.set_aspect('equal')

ax_fixed.set_xlim((-8, 8))
ax_fixed.set_ylim((-8, 8))

ax_rot.set_xlim((-8, 8))
ax_rot.set_ylim((-8, 8))

# Turn off axes
plt.axis('off')

plt.show()