import unittest
import Sim
import body as b
import numpy as np

class TestBody(unittest.TestCase):
    #This is uses to create a bunch of bodies for testing
    #                 mass,       x,         y,          x_velo,     y_velo
    SUN =     b.body(1.989e+30,   0,         0,          0,          0)
    MERCURY = b.body(0.33011e24,  57.909e9,  0,          0,          47.36e3)
    VENUS = b.body(4.8675e24,    -108.209e9, 0,          0,          35.02e3)
    EARTH =   b.body(5.97219e+24, 0,         148e9,      3e4,        0)
    MARS = b.body(0.64171e24,     161.166e9, 161.166e9,  17.02e3,    -17.02e3)
    JUPITER = b.body(1898.13e24,  0,        -778.57e9,  -13.06e3,    0)
    SATURN = b.body(568.34e24,    1013.66e9, -1013.66e9,-6.845e3,   -6.845e3)
    URANUS = b.body(86.8e24,      2872.46e9,  0,         0,          6.8e3)
    NEPTUNE = b.body(102.413e24,  -3178.49e9, 3178.49e9,  3.839e3,    3.839e3)
    
    #a list of bodies for testing
    full_local = [SUN,MERCURY,VENUS,EARTH,MARS,JUPITER,SATURN,URANUS,NEPTUNE]
    
    #a dt for testing
    test_dt = 60 * 60
    #a duration for testing 
    test_dur = 365 *24 *60 *60
    
    #This is testing the adjust_do_sizes from Sim
    def test_adjust_dot_sizes(self):
        #Get all the masses of all of the bodies into a list
        masses = [mass.mass for mass in self.full_local]
        
        #checking that the a size is returned for each dot 
        results = Sim.adjust_dot_sizes(masses)
        self.assertEqual(len(results), len(masses))
    
    #This is testing the orbit_sim from Sim
    def test_orbit_sim(self):
        #Testing the orbit_sim is returning the correct amount of values
        results = Sim.orbit_sim(self.full_local, self.test_dur, self.test_dt)
        self.assertEqual(len(results), 2)
        
    #This is testing the accl_all from Sim
    def test_accl_all(self):
        #Checking that the same amount of bodies that were passed in are returned
        results = Sim.accl_all(self.full_local, self.test_dt)
        self.assertEqual(len(results), len(self.full_local))
    
    #This is testing the move_all from Sim
    def test_move_all(self):
        #Checking that the same amount of bodies that were passed in are returned 
        results = Sim.move_all(self.full_local, self.test_dt)
        self.assertEqual(len(results), len(self.full_local))
    

if __name__ == '__main__':
    unittest.main()