import Sim
import matplotlib.pyplot as plt
import numpy as np
import body as b
#---------------------

years = 100
days = years *365

# duration is a length of years split into seconds
dur= days *24 *60*60
#measured in seconds one hour
hour = 3600

day = 24*hour

year = 365*hour

frame_time = 0.001
#---------------------


def distance_e_s():
    bodies = [Sim.SUN,Sim.EARTH]
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,hour)
    
    distances = []
    
    for bodies in b_list:
        distances.append(b.calc_square_distance(bodies[0],bodies[1])**0.5)
        
    plt.plot(range(len(distances)),distances,"green")
    plt.xlabel("time step")
    plt.ylabel("distance (m)")
    plt.title("Distance Between Earth and Sun Over 100 Years")
    
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,day)
    distances = []
    for bodies in b_list:
        distances.append(b.calc_square_distance(bodies[0],bodies[1])**0.5)
    
    plt.plot(range(len(distances)),distances, "red")
    
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,year)
    distances = []
    for bodies in b_list:
        distances.append(b.calc_square_distance(bodies[0],bodies[1])**0.5)
    
    plt.plot(range(len(distances)),distances, "black")
    

distance_e_s()