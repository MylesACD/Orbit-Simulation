import numpy as np


G = 6.67408e-11
EARTH = 5.97219e+24 
SUN = 1.989e+30

# 1 million km
DISTANCE_TOL = 1e9
class body(object):
    
    def __init__(self,mass,x,y,x_velo,y_velo):
        self.mass = mass
        self.y = y
        self.x = x
        self.y_velo = y_velo
        self.x_velo = x_velo
        

            
   
    def __str__(self):
        return str(self.mass)
        
    

def calc_square_distance(b1,b2):
    return ((b1.x - b2.x)**2 + (b1.y-b2.y)**2)

def print_bodies(bodies):
    for body in bodies:
        print(body)
        
def calc_velo(body,bodies,dt):
    if body.mass<1:
        return body
    

    for other in bodies:
        
        # do not process the relationship between a body and its self
        if body != other and other.mass>0:            
            r2 = calc_square_distance(body,other)
            
            # zero the body
            #calculate momentum shift
            if (r2**0.5) < DISTANCE_TOL:

                print(body.mass," collided with: ", other.mass)
                #return zero()
            
            if r2!=0:
            
                #magnitude of the accleration 
                accl = G * other.mass /r2 * dt
                # the x distance
                dx =other.x - body.x
                # the y distance
                dy = other.y - body.y
                # the euclidean distance
                d = r2**0.5
            
                # the x and y component of acceleration using soh-cah
                x_component = dx/d*accl
                y_component = dy/d*accl
                
                body.x_velo+=x_component
                body.y_velo+=y_component
      
        
            
    return body

def move(body,dt):
        body.x += body.x_velo *dt
        body.y += body.y_velo *dt
        return body
    
def zero():
    return body(0,0,0,0,0)