import numpy as np
import copy
G = 6.67408e-11


class body(object):
    
    def __init__(self,mass,x,y,x_velo,y_velo):
        self.mass = mass
        self.y = y
        self.x = x
        self.y_velo = y_velo
        self.x_velo = x_velo
        
    def calc_velo(self,bodies,dt):
        this= copy.copy(self)
        for other in bodies:
            if this.x!=other.x or this.y!=other.y:
                r2 = calc_square_distance(this,other)
                #magnitude of the accleration 
                accl = G * other.mass /r2
                theta = np.arctan2([this.y,other.y],[this.x,other.x])[0]
                #theta *= (180.0/np.pi)
                x_component = np.cos(theta)*accl
                y_component = np.sin(theta)*accl
                this.x_velo+=x_component *dt
                this.y_velo+=y_component *dt
            else:
                #TODO collision
                pass
            
            return this
            
    def move(self,dt):
        this=copy.copy(self)
        this.x += self.x_velo *dt
        this.y += self.y_velo *dt
        return this
    def __str__(self):
        return str(self.mass)
        


def calc_square_distance(b1,b2):
    return ((b1.x - b2.x)**2 + (b1.y-b2.y)**2)

