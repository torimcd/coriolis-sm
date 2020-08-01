#  Particle on a spheroid earth

""" 
This program shows the paths of particles on a spheroidal earth. The lefthand sphere is at rest in
absolute space, the right hand sphere is shown in a reference frame rotating with angular velocity w 

Code translated from GW-BASIC provided in Exercise 7.1 of Stommel and Moore (1989)

author: Victoria McDonald
email: vmcd@atmos.washington.edu
website: https://github.com/torimcd/coriolis-sm

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
w = 10         # rotation rate of the earth (angular velocity) (m/s) right hand sphere
w2 = w^2       # the bulge of the sphereoid - set to zero for a perfect sphere
dt = 0.005  
fact = 60      # scale of the display
inc = pi/16    # inclination of the spheres  
lat = {}          # latitude
lon = {}       # longitude
dlat = {}
dlon = {}
ddlat = {}
ddlon = {}
t=0
rho = {}
x = {}
y = {}
z = {}
c = {}

u = 0      # eastward velocity
v = 0      # northward velocity

# ---------------------------------------
# ask user for latitiude and u,v
latitude = 40 #input("Enter a latitude:  ")
(u, v) = 1,2 #input("Enter values for u, v: ")

print(u)
print(v)

# NOTE: python is zero based so the particles are stored as 0,1,2,3 instead of 1,2,3,4
# for ease of reading along with the book, index 1 has been kept as the expert in absolute space,
# index 2 has been kept as the novice in absolute space
# index 3 has been kept as the expert in  moving reference frame
# index 4 has been moved to index 0 - the novice in the moving reference frame

for i in range(4):
    lat[i] = latitude*pi/180
    lon[i] = -pi/2

dlat[1] = 0
dlat[3] = 0
dlat[2] = v
dlat[0] = dlat[2]

dlon[2] = u/np.cos(lat[1]) + w
dlon[0] = dlon[2]

# integration in absolute frame
ddlon[2] = 2*np.tan(lat[2])*dlat[2]*dlon[2]

aaa = np.sin(lat[2])*np.cos(lat[2])
bbb = (w2 - (dlon[2]))**2

ddlat[2] = aaa*bbb

dlon[2] = dlon[2] + dt*ddlon[2]
dlat[2] = dlat[2] + dt*ddlat[2]

t = t+dt

lat[2] = lat[2] + dt*dlat[2]
lon[2] = lon[2] + dt*dlon[2]

lon[0] = lon[2] - w*t

# integration in relative frame using x,y coordinates
lat[0] = lat[2]
lon[1] = lon[1] + w*dt

for i in range(4):
    rho[i] = np.cos(lat[i])
    x[i] = rho[i]*np.cos(lon[i])
    y[i] = rho[i]*np.sin(lon[i])*np.sin(inc)
    z[i] = y[i] + np.sin(lat[i])*np.cos(inc)

# set the color of the particle based on its position
if y[2] < 0:
    c[1] = 'red'
else:
    c[1] = 'green'

if y[2] < 0:
    c[2] = 'yellow'
else:
    c[2] = 'green'

if y[3] < 0:
    c[3] = 'red'
else:
    c[3] = 'green'

if y[0] < 0:
    c[0] = 'yellow'
else:
    c[0] = 'red'




# ------------------------------------------
# set up figure and animation

fig = plt.figure()

ax_fixed = fig.add_subplot(121, aspect='auto')

# create oblate spheroids out of ellipse patches for outline and lats
fixed_outline = patches.Ellipse((0,0), 60, 60, 0, linewidth=2, fill=False)
fixed_center_lat = patches.Ellipse((0,0), 60, 60*np.sin(inc), 0, linewidth=1, fill=False)

c9 = 30*np.sin(pi/6)*np.cos(inc)
c8 = 30*np.sin(pi/3)*np.cos(inc)

fixed_mid_lat_up = patches.Ellipse((0,0+c9), 60*np.cos(pi/6), 60*np.sin(inc), 0, linewidth=1, fill=False)
fixed_mid_lat_down = patches.Ellipse((0,0-c9), 60*np.cos(pi/6), 60*np.sin(inc), 0, linewidth=1, fill=False)
fixed_pole_lat_up = patches.Ellipse((0,0+c8), 60*np.cos(pi/3), 30*np.sin(inc), 0, linewidth=1, fill=False)
fixed_pole_lat_down = patches.Ellipse((0,0-c8), 60*np.cos(pi/3), 30*np.sin(inc), 0, linewidth=1, fill=False)

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
rot_outline = patches.Ellipse((0,0), 60, 60, 0, linewidth=2, fill=False)
rot_center_lat = patches.Ellipse((0,0), 60, 60*np.sin(inc), 0, linewidth=1, fill=False)

rot_mid_lat_up = patches.Ellipse((0,0+c9), 60*np.cos(pi/6), 60*np.sin(inc), 0, linewidth=1, fill=False)
rot_mid_lat_down = patches.Ellipse((0,0-c9), 60*np.cos(pi/6), 60*np.sin(inc), 0, linewidth=1, fill=False)
rot_pole_lat_up = patches.Ellipse((0,0+c8), 60*np.cos(pi/3), 30*np.sin(inc), 0, linewidth=1, fill=False)
rot_pole_lat_down = patches.Ellipse((0,0-c8), 60*np.cos(pi/3), 30*np.sin(inc), 0, linewidth=1, fill=False)

# add the ellipses to the plot
ax_rot.add_patch(rot_outline)
ax_rot.add_patch(rot_center_lat)
ax_rot.add_patch(rot_mid_lat_up)
ax_rot.add_patch(rot_mid_lat_down)
ax_rot.add_patch(rot_pole_lat_up)
ax_rot.add_patch(rot_pole_lat_down)

ax_rot.set_aspect('equal')

ax_fixed.set_xlim((-35, 35))
ax_fixed.set_ylim((-35, 35))

ax_rot.set_xlim((-35, 35))
ax_rot.set_ylim((-35, 35))

ax_fixed.set_title("Absolute")
ax_rot.set_title("Relative")

# Turn off axes
plt.axis('off')

plt.show()