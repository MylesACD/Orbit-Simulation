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


def distance_e_s(years):
    #divide by 100 to get a percentage
    measured_avg = 149.6e9/100
    
     
    bodies = Sim.full_local
    
    plt.xlabel("Year")
    plt.ylabel("Perecnt of Real Average Distance")
    title = "Distance Between Earth and Sun Over " +str(years)+ " Years" 
    plt.title(title)
  
    #distance for hour timestep
    distances = []
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,hour)
    for bodies in b_list:
        #percentage distance
        distances.append(b.calc_square_distance(bodies[0],bodies[3])**0.5 / measured_avg)
    xvals = np.asarray(range(len(distances)))/len(distances) * years
    plt.plot(xvals,distances,"green")

    #distance for day timestep
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,day)
    distances = []
    for bodies in b_list:
        #percentage distance
        distances.append(b.calc_square_distance(bodies[0],bodies[3])**0.5/ measured_avg)
    distances = np.repeat(distances,24)
    xvals = np.asarray(range(len(distances)))/len(distances)* years
    plt.plot(xvals,distances, "red")
    
     #distance for year timestep
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,year)
    distances = []
    for bodies in b_list:
        #percentage distance
        distances.append(b.calc_square_distance(bodies[0],bodies[3])**0.5/ measured_avg)
    distances = np.repeat(distances,365)
    xvals = np.asarray(range(len(distances)))/len(distances)*years
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
    plt.plot(xvals,yvals)

def sun_barycenter_distance(bodies,dur,dt):
     list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,dt)
     distances = []
     for bodies in b_list:
         sun = bodies[0]
         x,y = b.center_of_mass(bodies)
         #distance between the sun and the barycenter
         distance = ((x-sun.x)**2 + (y-sun.y)**2)**0.5
         distances.append(distance)
     xvals = np.asarray(range(len(distances)))/len(distances)*(dur/365/24/60/60)
     plt.title("Distance From Sun to Barycenter")
     plt.xlabel("Years")
     plt.ylabel("Distance (meters)")
     plt.plot(xvals,distances)
# plot earth's x and y velocity over a number of years     
def earth_velocity(dur,dt):
    bodies = Sim.full_local
    list_of_positions, b_list  = Sim.orbit_sim(bodies,dur,dt)
    xvelos=[]
    yvelos=[]
  
    for bodies in b_list:
        xvelos.append(bodies[3].x_velo)
        yvelos.append(bodies[3].y_velo)
    #put the x axis in years
    xvals = np.asarray(range(len(xvelos)))/len(yvelos)*(dur/365/24/60/60)
    plt.title("X and Y Velocities of Earth")
    plt.xlabel("Years")
    plt.ylabel("Velocity (meters/second)")
    plt.plot(xvals,xvelos)
    plt.plot(xvals,yvelos)
    
    
#distance_e_s(50)
#system_bary_center(Sim.full_local,dur,hour)
sun_barycenter_distance(Sim.S_E,dur,hour)
#earth_velocity(dur,hour)