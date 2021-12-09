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
    #divide by 100 to get year 
    measured_avg = 149.6e9/100 
    
    
    bodies = [Sim.SUN,Sim.EARTH]
    
    plt.xlabel("Year")
    plt.ylabel("Perecnt of Real Average Distance")
    plt.title("Distance Between Earth and Sun Over 100 Years")
  
    #distance for hour timestep
    distances = []
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,hour)
    for bodies in b_list:
        distances.append(b.calc_square_distance(bodies[0],bodies[1])**0.5 / measured_avg)
    xvals = np.asarray(range(len(distances)))/len(distances) *100
    plt.plot(xvals,distances,"green")

    #distance for day timestep
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,day)
    distances = []
    for bodies in b_list:
        distances.append(b.calc_square_distance(bodies[0],bodies[1])**0.5/ measured_avg)
    distances = np.repeat(distances,24)
    xvals = np.asarray(range(len(distances)))/len(distances)*100
    plt.plot(xvals,distances, "red")
    
     #distance for year timestep
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,year)
    distances = []
    for bodies in b_list:
        distances.append(b.calc_square_distance(bodies[0],bodies[1])**0.5/ measured_avg)
    distances = np.repeat(distances,365)
    xvals = np.asarray(range(len(distances)))/len(distances)*100
    plt.plot(xvals,distances, "black")
    
# show the path of the center of mass of the system over time
# should output a single dot as the C.O.M. doesn't move    
def system_bary_center(bodies,dur,dt):
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,dt)
    xvals = []
    yvals=[]
    i=0
    while i< len(b_list):
        bodies = b_list[i]
        x,y = b.center_of_mass(bodies)
        xvals.append(x)
        yvals.append(y)
        i+=1000
        
    plt.plot(xvals,yvals,"o")
    
    
#distance_e_s()
system_bary_center([Sim.SUN,Sim.EARTH],dur,day)