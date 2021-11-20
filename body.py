import numpy as np
import copy

G = 6.67408e-11
EARTH = 5.97219e+24 
SUN = 1.989e+30
DISTANCE_TOL = 1e2
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
    #bodies.remove(body)

    for other in bodies:
        if other.x - DISTANCE_TOL <= body.x<=other.x + DISTANCE_TOL and other.y - DISTANCE_TOL <=body.y<=other.y-DISTANCE_TOL and body.mass <other.mass:
            
                    return None
             
        
        
        # do not process the relationship between a body and its self
        if body != other:
            #do a collision if
            #
            
            r2 = calc_square_distance(body,other)
            #magnitude of the accleration 
            accl = G * other.mass /r2 * dt
            
            dx =other.x - body.x
            dy = other.y - body.y
            d = r2**0.5
            
         
            x_component = dx/d*accl
            y_component = dy/d*accl
            body.x_velo+=x_component
            body.y_velo+=y_component
      
        
            
    return body
    
def move(body,dt):
        body = copy.copy(body)
        body.x += body.x_velo *dt
        body.y += body.y_velo *dt
        return body