#  Particle on a spheroid earth

""" 
This program shows the paths of particles on a spheroidal earth. The lefthand sphere is at rest in
absolute space, the right hand sphere is shown in a reference frame rotating with angular velocity w 

Code adapted from GW-BASIC provided in Exercise 7.1 of Stommel and Moore (1989)

author: Victoria McDonald
email: vmcd@atmos.washington.edu
website: https://github.com/torimcd

"""

import matplotlib

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