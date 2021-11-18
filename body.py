import numpy as np
G = 6.67408e-11


class body(object):
    
    def __init__(self,mass,y,x,y_velo,x_velo):
        self.mass = mass
        self.y = y
        self.x = x
        self.y_velo = y_velo
        self.x_velo = x_velo
        
    def calc_velo(self,bodies,dt):
        
        for other in bodies:
            r2 = calc_square_distance(self,other)
            #magnitude of the accleration 
            accl = G * other.mass /r2
            theta = np.arctan2([self.y,other.y],[self.x,other.x])[0]
            #theta *= (180.0/np.pi)
            x_component = np.cos(theta)*accl
            y_component = np.sin(theta)*accl
            self.x_velo+=x_component *dt
            self.y_velo+=y_component *dt
            
            return self
            
    def move(self,dt):
        self.x += self.x_velo *dt
        self.y += self.y_velo *dt
        return self
        


def calc_square_distance(b1,b2):
    return ((b1.x - b2.x)**2 + (b1.y-b2.y)**2)

