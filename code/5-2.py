#  Oscillations in a vertical plane on three platforms

""" 
Code translated from GW-BASIC provided in Exercise 5.1 of Stommel and Moore (1989)

author: Victoria McDonald
email: vmcd@atmos.washington.edu
website: https://github.com/torimcd/coriolis-sm

"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np

# set up global variables
dt = 0.01   # time step
g = 1       # gravity
d = 1
k = 1       # spring constant
k2 = k**2
c = k2/2
a = k2/g
mu = 0    # angular momentum
r = {}
dr = {}
ddr = {}
p = {}
dp = {}
x = {}
y = {}

x_plane = []
y_plane = []
x_para = []
y_para = []
x_hemi = []
y_hemi = []
l_plane = []
l_para = []
l_hemi = []
m_plane = []
m_para = []
m_hemi = []

# set up the surfaces
for i in range(3):
    r[i] = 0.5
    dr[i] = 0
    p[i] = 0


# ------- Set up figure ------

fig = plt.figure(figsize=(10,8))

# create an axis for each surface
ax_1 = fig.add_subplot(231, aspect=1)
plt.axis('off')
ax_2 = fig.add_subplot(232, aspect=1)
plt.axis('off')
ax_3 = fig.add_subplot(233, aspect=1)
plt.axis('off')

# create an axis for each vertical section
ax_1_below = fig.add_subplot(234, aspect=0.5)
plt.axis('off')
ax_2_below = fig.add_subplot(235, aspect=0.5)
plt.axis('off')
ax_3_below = fig.add_subplot(236, aspect=0.5)
plt.axis('off')

# create outline
outline_1 = patches.Ellipse((0,0), 1, 1, 0, linewidth=2, fill=False)
outline_2 = patches.Ellipse((0,0), 1, 1, 0, linewidth=2, fill=False)
outline_3 = patches.Ellipse((0,0), 1, 1, 0, linewidth=2, fill=False)

# add outline to axes
ax_1.add_patch(outline_1)
ax_2.add_patch(outline_2)
ax_3.add_patch(outline_3)

ax_1.set_xlim(-0.6, 0.6)
ax_1.set_ylim(-0.6, 0.6)

ax_2.set_xlim(-0.6, 0.6)
ax_2.set_ylim(-0.6, 0.6)

ax_3.set_xlim(-0.6, 0.6)
ax_3.set_ylim(-0.6, 0.6)

ax_1_below.set_xlim(-1, 1)
ax_1_below.set_ylim(-1, 1)
ax_2_below.set_xlim(-1, 1)
ax_2_below.set_ylim(-1, 1)
ax_3_below.set_xlim(-1, 1)
ax_3_below.set_ylim(-1, 1)

plt.suptitle("Three Surfaces of Revolution")
ax_1_below.set_title("plane")
ax_2_below.set_title("paraboloid")
ax_3_below.set_title("hemisphere")


# set up the particles
plane = ax_1.plot([], [], color='green')[0]
paraboloid = ax_2.plot([], [], color='red')[0]
hemisphere = ax_3.plot([], [],  color='gold')[0]

plane_section = ax_1_below.plot([], [], color='green')[0]
paraboloid_section = ax_2_below.plot([], [], color='red')[0]
hemisphere_section = ax_3_below.plot([], [], color='gold')[0]


def update(frame):
    global dt
    global g
    global d
    global k
    global k2
    global c
    global a
    global mu
    global r
    global dr
    global ddr
    global p
    global dp
    global x
    global y

    global x_plane
    global y_plane
    global x_para
    global y_para
    global x_hemi
    global y_hemi
    global l_plane
    global l_para
    global l_hemi
    global m_plane
    global m_para
    global m_hemi

    # draw cross sections first
    if frame < 70:
        i_map = np.arange(-0.7, 0.7, 0.02)
        i = i_map[frame]
        
        l_plane.append(i)
        m_plane.append(0)

        l_para.append(i)
        m_para.append(c*(i**2))

        if (a**2 - i**2) <= 0:
            plane_section.set_data(l_plane[:], m_plane[:])
            paraboloid_section.set_data(l_para[:], m_para[:])
            hemisphere_section.set_data(l_hemi[:], m_hemi[:])

        else:
            l_hemi.append(i)

            m_hemi.append(a-np.sqrt(a**2 - i**2))
                
            plane_section.set_data(l_plane[:], m_plane[:])
            paraboloid_section.set_data(l_para[:], m_para[:])
            hemisphere_section.set_data(l_hemi[:], m_hemi[:])
            

    else: 
        # integrations for plan view
        ddr[1] = mu**2/(r[1]**3)-k**2*r[1]
    
        aaa = (1+(2*c*r[2])**2)
        ccc = mu**2/(r[2]**3)
        bbb = -2*g*r[2] - r[2]*(2*c*dr[2])**2

        ddr[2] = (bbb+ccc)/aaa

        aa = -g*r[0]/(np.sqrt(a**2 - r[0]**2))
        cc = (-dr[0]**2)*(a**2*r[0]/((a**2-r[0]**2)**2))
        dd = 1+r[0]**2/(a**2*r[0]**2)
        bb = mu**2/(r[0]**3)

        ddr[0] = (aa+bb+cc)/dd

        for i in range(3):
            dr[i] = ddr[i]*dt + dr[i]
            r[i] = dr[i]*dt + r[i]

        for i in range(3):
            dp[i] = mu/(r[i]**2)
            p[i] = dp[i]*dt + p[i]

        for i in range(3):
            x[i] = r[i]*np.cos(p[i])
            y[i] = r[i]*np.sin(p[i])

        x_plane.append(r[1]*np.cos(p[1]))
        y_plane.append(r[1]*np.sin(p[1]))

        x_para.append(r[2]*np.cos(p[2]))
        y_para.append(r[2]*np.sin(p[2]))

        x_hemi.append(r[0]*np.cos(p[0]))
        y_hemi.append(r[0]*np.sin(p[0]))

        plane.set_data(x_plane[:], y_plane[:])
        paraboloid.set_data(x_para[:], y_para[:])
        hemisphere.set_data(x_hemi[:], y_hemi[:])


        
# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, update, frames=1000, interval=10, repeat=False, blit=False)

plt.show()