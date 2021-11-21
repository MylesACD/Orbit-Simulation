import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import body as b


#---------------------
dur=50000
#seconds in a day
dt = 60*60*24



#---------------------
EARTH =   b.body(5.97219e+24, 0,         148e9,  3e4,  0 )
SUN =     b.body(1.989e+30,   0,         0,      0,    0)
JUPITER = b.body(1898.19e24,  778.57e9,  0,      0,    1.306e4)
XTE_J =   b.body(5.967e30,   -400e9,    -400e9,  2e4,  2e4)

#return a 3d array should be shape dur,2,len(bodies)
def orbit_sim(bodies,dur,dt):
    positions = []
    positions.append(construct_points(bodies))
    
    for i in range(dur):
        #print_bodies(bodies)
        bodies = accl_all(bodies,dt)
        bodies = move_all(bodies,dt)
        positions.append(construct_points(bodies)) 
    return positions

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
    
    
def anim_orbit(bodies,dur,dt):
    list_of_positions =np.asarray(orbit_sim(bodies,dur,dt))
    
    plot_interval = list_of_positions.shape[0]//220
    
    masses = [body.mass for body in bodies]
    dots = adjust_dot_sizes(masses)

    xmin = np.min(list_of_positions[:,0,:])
    ymin= np.min(list_of_positions[:,1,:])
    xmax= np.max(list_of_positions[:,0,:])
    ymax= np.max(list_of_positions[:,1,:])
    
    
    #------render setup
    #plt.get_current_fig_manager().window.showMaximized() 
    fig, ax = plt.subplots()
    fig.canvas.draw()
    ax.plot([],[],"o")
    plt.pause(0.001) 
    
    #-----------------------

    # skip frames
    i=0
    while i < list_of_positions.shape[0]:
        space = list_of_positions[i]
        ax.clear()
        ax.set(xlim=([xmin*1.1,xmax*1.1]),ylim=[ymin*1.1,ymax*1.1])
        ax.scatter(space[0],space[1],s=dots)
        ax.set_yscale("linear")
        ax.set_xscale("linear")
        ax.axis("off")
        ax.draw(fig.canvas.renderer)
        plt.pause(0.001) 
        i+=plot_interval

       
            
        
    
def adjust_dot_sizes(masses):
    mexp = [str(mass).split("e+")[1] for mass in masses]
    mexp =np.asarray([int(num) for num in mexp])
    mexp = mexp/min(mexp)
    mexp = mexp**4
    mexp = [20*2**num for num in mexp]
    print(mexp)
    return mexp

    
   
    

        
        

    
test1 = [EARTH,SUN,JUPITER,XTE_J]
test2 = [EARTH,XTE_J]
anim_orbit(test2,dur,dt)
#orbit_sim(testing, dur, dt)
        
        
    
   
     

