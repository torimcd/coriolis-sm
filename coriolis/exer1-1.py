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

class Particle:
    ''' Particle Class

    init_state is the initial state [dxdt, dydt]
    where dxdt, dydt are the x and y velocities of the particle
    '''

    def __init__(self,
                init_state = [1, 1, 0, 0],
                x=0, #initial position at origin
                y=0,
                force_x_dir=0, #initial force is zero
                force_y_dir=0):
        self.init_state = np.asarray(init_state, dtype='float')
        self.params = (x, y, force_x_dir, force_y_dir)
        self.time_elapsed = 0

        self.state = self.init_state


    def position(self):
        ''' compute the current x,y position of the particle '''
        (x, y, force_x_dir, force_y_dir) = self.params

    def step(self, dt):
        ''' execute one time step and update state'''
        self.time_elapsed += dt
        

    def calc_derivatives(self, state, t):
        '''
        Compute the first and second derivatives given the current position, current forcing
        -----------
        Parameters:
        franme: the current frame of the animation, used as time step
        x: the current x position of the particle
        y: the current y position of the particle
        force_x: the foring in the x-direction
        force_y: the forcing in the y-direction
        --------
        Returns: the next x and y position
        '''

        if frame < (11):
            force_x = 0
            force_y = 0

            #x_arrow = 0
            #y_arrow = 0
            #dx_arrow = 0
            #dy_arrow = 0
        else:
            force_x = force_x_direction
            force_y = force_y_direction

            #x_arrow = 150
            #y_arrow = 120
            #dx_arrow = x_arrow + force_scaling_factor*force_x_direction
            #dy_arrow = 120 - force_scaling_factor*force_y_direction

        
        # initial values for the second derivatives
        d2xdt2 = force_x
        d2ydt2 = force_y

        # here are the equations of motion
        dxdt = d2xdt2 + dxdt
        dydt = d2ydt2 + dydt

        x = dxdt + x
        y = dydt + y

        return (dxdt, dydt), (d2xdt2, d2ydt2)


#---------------------------------------------
# set up initial state and global variables
particle = Particle(0,0)
dt = 1./30  # 30 frames per second


#---------------------------------------------
# create the figure
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', xlim=(-10, 10), ylim=(-10,10))

# initialize some variables
arrow_scaling_factor = 10   # FAC in BASIC
force_scaling_factor = 10   # FFF in BASIC
trajectory_scaling_factor = 10  # FFC in BASIC 

# set the initial position of the particle at the origin
x=0
y=0

# set random initial values for dx and dy
dxdt = trajectory_scaling_factor*(tools.rnd()-0.5)
dydt = trajectory_scaling_factor*(tools.rnd()-0.5)

force_x_direction = force_scaling_factor*(tools.rnd()-0.5)
force_y_direction = force_scaling_factor*(tools.rnd()-0.5)

# arrow length is the hypotenuse of the forces in the x and y direction
arrow_length = np.hypot(force_scaling_factor*force_x_direction, force_scaling_factor*force_y_direction)

# draw the particle and arrow
position, = ax.plot([],[], 'ro')
#arrow = ax.arrow(0, 0, 0, 0)
#a = ax.add_patch(arrow)


def init():
    '''Initialize animation'''
    # set up empty objects for the particle and arrow
    line.set_data([],[])
    return line,

def animate(frame):
    ''' Do the animation '''
    global particle, dt
    particle.step(dt)

    line.set_data(*particle.position())
    return line, 


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=20, interval=500, blit=True)
plt.show()