import unittest
import body as b
import gui

class TestBody(unittest.TestCase):
    #                 mass,       x,         y,          x_velo,     y_velo
    SUN =     b.body(1.989e+30,   0,         0,          0,          0)
    MERCURY = b.body(0.33011e24,  57.909e9,  0,          0,          47.36e3)
    VENUS = b.body(4.8675e24,    -108.209e9, 0,          0,          35.02e3)
    EARTH =   b.body(5.97219e+24, 0,         148e9,      3e4,        0)   
    
    def test_body_to_string(self):       
        results = gui.body_to_string(self.SUN)
        self.assertGreater(len(results), 0)
        
        results = gui.body_to_string(self.EARTH)
        self.assertGreater(len(results), 0)
        
        results = gui.body_to_string(self.MERCURY)
        self.assertGreater(len(results), 0)
        
        results = gui.body_to_string(self.VENUS)
        self.assertGreater(len(results), 0)

if __name__ == '__main__':
    unittest.main()
