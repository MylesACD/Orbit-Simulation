import Sim
import matplotlib.pyplot as plt
import numpy as np
import body as b
#---------------------

years = 10
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
    measured_avg = 149.6e9
    
    
    bodies = Sim.full_local
    
    plt.xlabel("Year")
    plt.ylabel("Perecnt of Real Average Distance")
    plt.title("Distance Between Earth and Sun Over 100 Years")
  
    #distance for hour timestep
    distances = []
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,hour)
    for bodies in b_list:
        distances.append(b.calc_square_distance(bodies[0],bodies[3])**0.5 / measured_avg)
    xvals = np.asarray(range(len(distances)))/len(distances) *100
    print(distances[0])
    plt.plot(xvals,distances,"green")

    #distance for day timestep
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,day)
    distances = []
    for bodies in b_list:
        distances.append(b.calc_square_distance(bodies[0],bodies[3])**0.5/ measured_avg)
    distances = np.repeat(distances,24)
    xvals = np.asarray(range(len(distances)))/len(distances)*100
    plt.plot(xvals,distances, "red")
    
     #distance for year timestep
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,year)
    distances = []
    for bodies in b_list:
        distances.append(b.calc_square_distance(bodies[0],bodies[3])**0.5/ measured_avg)
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
    plt.title("Center of Mass Path")
    plt.plot(xvals,yvals,"o")

def sun_barycenter_distance(bodies):
     list_of_positions, b_list  = Sim.orbit_sim(bodies,50*365*24*60*60,hour)
     distances = []
     for bodies in b_list:
         sun = bodies[0]
         x,y = b.center_of_mass(bodies)
         #distance between the sun and the barycenter
         distance = ((x-sun.x)**2 + (y-sun.y)**2)**0.5
         distances.append(distance)
     xvals = np.asarray(range(len(distances)))/len(distances)*50
     plt.title("Distance From Sun to Barycenter Over 50 Years")
     plt.xlabel("Years")
     plt.ylabel("Distance (meters)")
     plt.plot(xvals,distances)
     
def earth_velocity():
    pass
    
distance_e_s()
#system_bary_center([Sim.SUN,Sim.EARTH],dur,day)
#sun_barycenter_distance(Sim.S_E)