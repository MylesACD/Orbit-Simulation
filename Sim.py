import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import body as b


#---------------------

years = 1
days = years *365

# duration is a length of years split into hours
dur= days *24
#one hour
dt = 60 *60


frame_time = 0.001

#---------------------
SUN =     b.body(1.989e+30,   0,         0,          0,          0)
MERCURY = b.body(0.33011e24,  57.909e9,  0,          0,          47.36e3)
VENUS = b.body(4.8675e24,    -108.209e9, 0,          0,          35.02e3)
EARTH =   b.body(5.97219e+24, 0,         148e9,      3e4,        0)
MARS = b.body(0.64171e24,     161.166e9, 161.166e9,  17.02e3,    -17.02e3)
JUPITER = b.body(1898.13e24,  0,        -778.57e9,  -13.06e3,    0)
SATURN = b.body(568.34e24,    1013.66e9, -1013.66e9,-6.845e3,   -6.845e3)
URANUS = b.body(86.8e24,      2872.46e9,  0,         0,          6.8e3)
NEPTUNE = b.body(102.413e24,  -3178.49e9, 3178.49e9,  3.839e3,    3.839e3)

XTE_J =   b.body(5.967e30,   -400e9,    -400e9,     1e3,  1e3)

#return a 3d array should be shape dur,2,len(bodies)
def orbit_sim(bodies,dur,dt):
    positions = []
    positions.append(construct_points(bodies))
    
    for i in range(int(dur)):
        #print_bodies(bodies)
        bodies = accl_all(bodies,dt)
        bodies = move_all(bodies,dt)
        positions.append(construct_points(bodies)) 
    return positions, bodies

def accl_all(bodies,dt):
    new_bodies = []
    for body in bodies:
        temp = b.calc_velo(body,bodies,dt)
        if type(temp)!=None:
            new_bodies.append(temp)
        else:
            bodies =bodies.remove(body)
        
    return new_bodies

def move_all(bodies,dt):
    new_bodies =[]
    for body in bodies:
       new_bodies.append(b.move(body,dt))
       
    return new_bodies
        
#returns a 2d array should be shape 2,len(bodies)
def construct_points(bodies):
    #points contains 2 arrays, [0] is x coords, [1] is y
    points = []
    x =[]
    y=[]
    for body in bodies:
        x.append(body.x)
        y.append(body.y)
        
    points.append(x)
    points.append(y)
    return points
    
    
def anim_orbit(bodies,dur,dt, speed):
    
    list_of_positions, end_bodies =orbit_sim(bodies,dur,dt)
    list_of_positions = np.asarray(list_of_positions)
    
    magic=  220
    if speed =="normal":
        plot_interval = list_of_positions.shape[0]//magic
    elif speed == "fast":
        plot_interval = list_of_positions.shape[0]//(magic//3)
    elif speed == "slow":
        plot_interval = list_of_positions.shape[0]//(magic*3)
    elif speed == "vfast":
        plot_interval = list_of_positions.shape[0]//(magic//9)
    elif speed == "efast":
        plot_interval = list_of_positions.shape[0]//(magic//25)
    #--------test code not to be included in final
   # print(end_bodies[0].x,"   ",end_bodies[0].y)
    
    #----------------------------------------------
   

    xmin = 1.5* np.min(list_of_positions[:,0,:])
    ymin= 1.5* np.min(list_of_positions[:,1,:])
    xmax= 1.5* np.max(list_of_positions[:,0,:])
    ymax= 1.5* np.max(list_of_positions[:,1,:])
    
    #------render setup
    
    fig, ax = plt.subplots()
    fig.canvas.draw()
    ax.plot([],[],"o")
    plt.pause(frame_time) 
    masses = [body.mass for body in bodies]
    dots = adjust_dot_sizes(masses)
    #fig.set_size_inches(figsize=(5,5))
    plt.get_current_fig_manager().window.showMaximized() 
    
    
    #-----------------------

    # skip frames
    i=0
    while i < list_of_positions.shape[0]:
        
        space = list_of_positions[i]
        ax.clear()
        ax.set(xlim=([xmin,xmax]),ylim=[ymin,ymax])
        ax.scatter(space[0],space[1],s=dots)
        ax.set_yscale("linear")
        ax.set_xscale("linear")
        ax.axis("off")
        ax.draw(fig.canvas.renderer)
        plt.pause(frame_time) 
        i+=plot_interval    
        
    
def adjust_dot_sizes(masses):
    #standarize the masses into scientific notation
    masses = ["{:.2e}".format(mass) for mass in masses]
    # extract the mass coe
    mcoe = [mass.split("e+")[0] for mass in masses]
    # the main size of the dot is based on the exponent of its mass
    mexp = [mass.split("e+")[1] for mass in masses]
    # convert strings to ints
    mexp =np.asarray([int(num) for num in mexp])
    mcoe = np.asarray([float(num) for num in mcoe])
    # get the ratio between the exponent and the smallest body exponent
    mexp = mexp/min(mexp)
    # put to the power of 5 to make it really matter
    mexp = mexp**5
    # mcoe is not as import as mexp, so reduce its power
    mcoe = mcoe**0.33
    # combine mcoe and mexp to form the sizes of the dots
    sizes = [15*2**num for num in mexp] * mcoe
    
    return sizes
  

full_local = [SUN,MERCURY,VENUS,EARTH,MARS,JUPITER,SATURN,URANUS,NEPTUNE,XTE_J]
test3 = [SUN,EARTH,MARS,JUPITER,MERCURY,VENUS]
test2 = [SUN,EARTH,JUPITER]
test1 = [EARTH,XTE_J]
#anim_orbit(test3, dur, dt)
anim_orbit(full_local,dur,dt, "normal")
#anim_orbit(test2,dur,dt)
#orbit_sim(testing, dur, dt)
        
        
    
   
     

