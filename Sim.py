import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import body as b


#---------------------
dur=1000
#seconds in a day
dt = 60*60*24



#---------------------
EARTH =b.body( 5.97219e+24,0,148e9,3e4,0 )
SUN = b.body(1.989e+30,0,0,0,0)
JUPITER = b.body(1898.19e24,778.57e9,0,0,13.06e3)

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
        
        new_bodies.append(b.calc_velo(body,bodies,dt))
        
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
 
    fig, ax = plt.subplots()
    plt.get_current_fig_manager().window.showMaximized() 
    xmin = np.min(list_of_positions[:,0,:])
    ymin= np.min(list_of_positions[:,1,:])
    xmax= np.max(list_of_positions[:,0,:])
    ymax= np.max(list_of_positions[:,1,:])
    
    ax.axis("off")
    for space in list_of_positions:
       # print(space)
        plt.clf()
        plt.xlim([xmin,xmax])
        plt.ylim([ymin,ymax])
        plt.plot(space[0],space[1],"o")
        plt.draw()
        #plt.pause(0.001)
       
            
        
    
 
   
    

        
        

    
testing = [EARTH,SUN,JUPITER]

anim_orbit(testing,dur,dt)
#orbit_sim(testing, dur, dt)
        
        
    
   
     

