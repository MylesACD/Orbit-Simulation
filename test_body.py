import unittest
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
    
    #This is testing the calc_square_distance function from body
    def test_calc_square_distance(self):   
        #Testing that the Sun and Earth distance is correct
        results = b.calc_square_distance(self.SUN, self.EARTH)
        self.assertEqual(results, 2.1904e+22)
        
        #Testing that the Venus and Mars distance is correct
        results = b.calc_square_distance(self.VENUS, self.MARS)
        self.assertEqual(results, 9.8537370181e+22)
        
        #Testing that the Neptune and Uranus distance is correct
        results = b.calc_square_distance(self.NEPTUNE, self.URANUS)
        self.assertEqual(results, 4.67167945826e+25)
        
        #Testing that the Jupiter and Mars distance is correct
        results = b.calc_square_distance(self.JUPITER, self.MARS)
        self.assertEqual(results, 9.09078229252e+23)
    
    #This is testing the calc_velo function from body
    def test_calc_velo(self):
        #Testing that the velocity for the sun is correct
        results = b.calc_velo(self.SUN, self.full_local, self.test_dt)
        self.assertEqual(results.x_velo, -2.5475595568412796e-05)
        self.assertEqual(results.y_velo, -0.0007308751743761587)
        
        #Testing that the velocity for the earth is correct
        results = b.calc_velo(self.EARTH, self.full_local, self.test_dt)
        self.assertEqual(results.x_velo, 30000.00002585143)
        self.assertEqual(results.y_velo, -21.818118165978927)
        
        #Testing that the velocity for the jupiter is correct
        results = b.calc_velo(self.JUPITER, self.full_local, self.test_dt)
        self.assertEqual(results.x_velo, -13059.999875694239)
        self.assertEqual(results.y_velo, 0.7883526501415731)
        
        #Testing that the velocity for the saturn is correct
        results = b.calc_velo(self.SATURN, self.full_local, self.test_dt)
        self.assertEqual(results.x_velo, -6845.16484438578)
        self.assertEqual(results.y_velo, -6844.835464408262)
        
    #This is testing the move function from body    
    def test_move(self):
        #testing that the move returns the mass to see if its the correct body
        results = b.move(self.VENUS, self.test_dt)
        self.assertEqual(results.mass, self.VENUS.mass)
        
        #testing that the move returns the mass to see if its the correct body
        results = b.move(self.EARTH, self.test_dt)
        self.assertEqual(results.mass, self.EARTH.mass)
        
    #This is testing the center of mass function from body
    def test_center_of_mass(self):
        #This is checking that the center of mass returns the correct number of values
        results = b.center_of_mass(self.full_local)
        self.assertEqual(len(results), 2)

if __name__ == '__main__':
    unittest.main()