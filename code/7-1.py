#  Particle on a spheroid earth

""" 
This program shows the paths of particles on a spheroidal earth. The lefthand sphere is at rest in
absolute space, the right hand sphere is shown in a reference frame rotating with angular velocity w 

Code translated from GW-BASIC provided in Exercise 7.1 of Stommel and Moore (1989)

author: Victoria McDonald
email: vmcd@atmos.washington.edu
website: https://github.com/torimcd/coriolis-sm

"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np

# ---------------------------------------
# ask user for latitiude and u,v

latitude_in = input("Enter a latitude:  ")
u_in = input("Enter a value for u: ")
v_in = input("Enter a value for v: ")

latitude = float(latitude_in)
u = float(u_in)
v = float(v_in)

# -----------------------------------------
# set up global variables

pi = np.pi    # pi
w = 10         # rotation rate of the earth (angular velocity) (m/s) right hand sphere
w2 = w**2       # the bulge of the sphereoid - set to zero for a perfect sphere
dt = 0.005     # time step
fact = 60      # scale of the display
inc = pi/16    # inclination of the spheres  
lat = {}       # latitude
lon = {}       # longitude
dlat = {}      # time derivative of latitude
dlon = {}      # time derivative of longitude
ddlat = {}     # acceleration in latitude
ddlon = {}     # acceleration in longitude
rho = {}
x = {}
y = {}
z = {}
c = {}      # colors for plotting

t = 0      # initial time is zero 

for i in range(4):
    lat[i] = latitude*pi/180
    lon[i] = -pi/2

dlat[1] = 0
dlat[3] = 0
dlat[2] = v
dlat[0] = dlat[2]

# convert u, v to velocities in absolute reference frame
dlon[2] = u/np.cos(lat[1]) + w
dlon[0] = dlon[2]


# ------------------------------------------
# set up figure

fig = plt.figure()

# -------- Create the sphere in the absolute reference frame
ax_fixed = fig.add_subplot(121, aspect='auto')

# create oblate spheroids out of ellipse patches for outline and lats
fixed_outline = patches.Ellipse((0,0), 120, 120, 0, linewidth=2, fill=False)
fixed_center_lat = patches.Ellipse((0,0), 120, 120*np.sin(inc), 0, linewidth=1, fill=False)

c9 = 60*np.sin(pi/6)*np.cos(inc)
c8 = 60*np.sin(pi/3)*np.cos(inc)

fixed_mid_lat_up = patches.Ellipse((0,0+c9), 120*np.cos(pi/6), 120*np.sin(inc), 0, linewidth=1, fill=False)
fixed_mid_lat_down = patches.Ellipse((0,0-c9), 120*np.cos(pi/6), 120*np.sin(inc), 0, linewidth=1, fill=False)
fixed_pole_lat_up = patches.Ellipse((0,0+c8), 120*np.cos(pi/3), 60*np.sin(inc), 0, linewidth=1, fill=False)
fixed_pole_lat_down = patches.Ellipse((0,0-c8), 120*np.cos(pi/3), 60*np.sin(inc), 0, linewidth=1, fill=False)

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

ax_fixed.set_xlim((-70, 70))
ax_fixed.set_ylim((-70, 70))

ax_fixed.set_title("Absolute")
# --------

# -------- Create the sphere in the rotating reference frame
ax_rot = fig.add_subplot(122, aspect='auto')

# create ellipse patches for the outline and lats
rot_outline = patches.Ellipse((0,0), 120, 120, 0, linewidth=2, fill=False) # sphere outline
rot_center_lat = patches.Ellipse((0,0), 120, 120*np.sin(inc), 0, linewidth=1, fill=False) # center lat ellipse

rot_mid_lat_up = patches.Ellipse((0,0+c9), 120*np.cos(pi/6), 120*np.sin(inc), 0, linewidth=1, fill=False) # mid lat ellipses
rot_mid_lat_down = patches.Ellipse((0,0-c9), 120*np.cos(pi/6), 120*np.sin(inc), 0, linewidth=1, fill=False)
rot_pole_lat_up = patches.Ellipse((0,0+c8), 120*np.cos(pi/3), 60*np.sin(inc), 0, linewidth=1, fill=False) # pole lat ellipses
rot_pole_lat_down = patches.Ellipse((0,0-c8), 120*np.cos(pi/3), 60*np.sin(inc), 0, linewidth=1, fill=False)

# add the ellipses to the plot
ax_rot.add_patch(rot_outline)
ax_rot.add_patch(rot_center_lat)
ax_rot.add_patch(rot_mid_lat_up)
ax_rot.add_patch(rot_mid_lat_down)
ax_rot.add_patch(rot_pole_lat_up)
ax_rot.add_patch(rot_pole_lat_down)

ax_rot.set_aspect('equal')

# Turn off axes
plt.axis('off')

ax_rot.set_xlim((-70, 70))
ax_rot.set_ylim((-70, 70))

ax_rot.set_title("Relative")
# --------


# set up the four particles
fixed_expert = ax_fixed.plot([], [], marker='o', ms=5, label='Expert')[0]
fixed_novice = ax_fixed.plot([], [], marker='o', ms=4, label='Novice')[0]
rotating_expert = ax_rot.plot([], [], marker='o', ms=5)[0]
rotating_novice = ax_rot.plot([], [], marker='o', ms=4)[0]

# ------ Set up legend 
ax_fixed.annotate('Expert: ', (-70, -60), color='k', weight='bold', fontsize=8)
ax_fixed.annotate('Novice: ', (-70, -70), color='k', weight='bold', fontsize=8)

ax_fixed.plot(-33, -57, color='red', marker='o', ms=5)
ax_fixed.plot(-33, -68, color='gold', marker='o', ms=4)

ax_fixed.annotate('On back, expert: ', (45, -60), color='k', weight='bold', fontsize=8)
ax_fixed.annotate('               novice: ', (45, -70), color='k', weight='bold', fontsize=8)

ax_rot.plot(-45, -57, color='green', marker='o', ms=5)
ax_rot.plot(-45, -68, color='limegreen', marker='o', ms=4)


# ------------------------------------------------
# set up the animation and methods for advancing the particles

def update(frame):
    global lat
    global lon
    global dlat
    global dlon
    global ddlat
    global ddlon
    global rho
    global x
    global y
    global z
    global t
    global u
    global v
    global w
    global w2
    global dt
    global fact


    # NOTE: python is zero based so the particles are stored as 0,1,2,3 instead of 1,2,3,4
    # for ease of reading along with the book, 
    # index 1 has been kept as the expert in absolute space,
    # index 2 has been kept as the novice in absolute space
    # index 3 has been kept as the expert in  moving reference frame
    # index 4 has been moved to index 0 - the novice in the moving reference frame



    # integration in absolute frame
    ddlon[2] = 2*np.tan(lat[2])*dlat[2]*dlon[2]

    aaa = np.sin(lat[2])*np.cos(lat[2])
    bbb = (w2 - (dlon[2])**2)

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
        c[2] = 'gold'
    else:
        c[2] = 'limegreen'

    if y[3] < 0:
        c[3] = 'red'
    else:
        c[3] = 'green'

    if y[0] < 0:
        c[0] = 'gold'
    else:
        c[0] = 'limegreen'


    fixed_expert.set_data(fact*x[1], fact*z[1])
    fixed_expert.set_color(c[1])

    fixed_novice.set_data(fact*x[2], fact*z[2])
    fixed_novice.set_color(c[2])

    rotating_expert.set_data(fact*x[3], fact*z[3])
    rotating_expert.set_color(c[3])
    
    rotating_novice.set_data(fact*x[0], fact*z[0])
    rotating_novice.set_color(c[0])

    return [fixed_expert, fixed_novice, rotating_expert, rotating_novice]


# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, update, frames=200, interval=70, repeat=False, blit=False)


plt.show()