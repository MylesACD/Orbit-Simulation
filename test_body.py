import unittest
import body as b
import numpy as np

class TestBody(unittest.TestCase):
    SUN =     b.body(1.989e+30,   0,         0,          0,          0)
    MERCURY = b.body(0.33011e24,  57.909e9,  0,          0,          47.36e3)
    VENUS = b.body(4.8675e24,    -108.209e9, 0,          0,          35.02e3)
    EARTH =   b.body(5.97219e+24, 0,         148e9,      3e4,        0)
    MARS = b.body(0.64171e24,     161.166e9, 161.166e9,  17.02e3,    -17.02e3)
    JUPITER = b.body(1898.13e24,  0,        -778.57e9,  -13.06e3,    0)
    SATURN = b.body(568.34e24,    1013.66e9, -1013.66e9,-6.845e3,   -6.845e3)
    URANUS = b.body(86.8e24,      2872.46e9,  0,         0,          6.8e3)
    NEPTUNE = b.body(102.413e24,  -3178.49e9, 3178.49e9,  3.839e3,    3.839e3)

    full_local = [SUN,MERCURY,VENUS,EARTH,MARS,JUPITER,SATURN,URANUS,NEPTUNE]
    
    def test_calc_square_distance(self):
        
        results = b.calc_square_distance(SUN, EARTH)
        self.assertEqual(results, second)

