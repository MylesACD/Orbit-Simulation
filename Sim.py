import matplotlib.pyplot as plt
import numpy as np
import body


#---------------------
dur=300
dt = 1



#---------------------
EARTH = 5.97219e+24 
SUN = 1.989e+30


#return a 3d array should be shape dur//dt,2,len(bodies)
def orbit_sim(bodies,dur,dt):
    positions = []
    positions.append(construct_points(bodies))
    for i in range(dur//dt):
       bodies = accl_all(bodies,dt)
       bodies = move_all(bodies,dt)
       positions.append(construct_points(bodies)) 
    return np.asarray(positions)

def accl_all(bodies,dt):
    new_bodies = []
    for body in bodies:
        new_bodies.append(body.calc_velo(bodies,dt))
        
        
    return new_bodies

def move_all(bodies,dt):
    new_bodies =[]
    for body in bodies:
       new_bodies.append(body.move(dt))
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
    list_of_positions = orbit_sim(bodies,dur,dt)
    
    for positions in list_of_positions:
        plt.plot(positions[0],positions[1],"o")
        
    
   
     

