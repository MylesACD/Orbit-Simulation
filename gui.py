import tkinter as tk 
import body as b
import Sim

root = tk.Tk()
root.title("Orbit Simulation")

#This is a temp holding places for the bodies that are created from the slider
list_of_all_bodies = []

#This is to hold the type of speed the sim will go by
speed_for_sim = tk.StringVar()
speed_for_sim.set("fast")

#This is to hold the type of time step
time_step = tk.IntVar()
time_step.set(60 * 60)

#---------------------
SUN =     b.body(1.989e+30,   0,         0,          0,          0)
MERCURY = b.body(0.33011e24,  57.909e9,  0,          0,          47.36e3)
VENUS = b.body(4.8675e24,    -108.209e9, 0,          0,          35.02e3)
EARTH =   b.body(5.97219e+24, 0,         148e9,      3e4,        0)
MARS = b.body(0.64171e24,     161.166e9, 161.166e9,  17.02e3,    -17.02e3)
JUPITER = b.body(1898.13e24,  0,        -778.57e9,  -13.06e3,    0)
SATURN = b.body(568.34e24,    1013.66e9, -1013.66e9,-6.845e3,   -6.845e3)
URANUS = b.body(86.8e24,      2872.46e9,  0,         0,          6.8e3)
NEPTUNE = b.body(102.413e24,  -3178.49e9, 3178.49e9,  3.839e3,    3.839e3)

XTE_J =   b.body(5.967e30,   -400e9,    -400e9,     1e3,  1e3)

full_local = [SUN,MERCURY,VENUS,EARTH,MARS,JUPITER,SATURN,URANUS,NEPTUNE]
local_plus = [SUN,MERCURY,VENUS,EARTH,MARS,JUPITER,SATURN,URANUS,NEPTUNE,XTE_J]
earth_sun = [SUN,EARTH]
earth_sun_jupter = [SUN, EARTH, JUPITER]


#-------------------------------------------------

#This is used to add our solar system into the list of bodies
def solar_preset():
    error_label.config(text="")
    if len(list_of_all_bodies) == 0: 
        list_of_all_bodies.extend(full_local)
        display_list()
    else:
        error_label.config(text="Sorry, can only add any preset once per a simulation. Please clear the list if you want to add a different preset.")

#This is used add our solar system with a black hole into the list of bodies
def solar_preset_plus():
    error_label.config(text="")
    if len(list_of_all_bodies) == 0:
        list_of_all_bodies.extend(local_plus)
        display_list()
    else:
        error_label.config(text="Sorry, can only add any preset once per a simulation. Please clear the list if you want to add a different preset.")

#This is used to add earth_sun into the list of bodies
def earth_sun_preset():
    error_label.config(text="")
    if len(list_of_all_bodies) == 0: 
        list_of_all_bodies.extend(earth_sun)
        display_list()
    else:
        error_label.config(text="Sorry, can only add any preset once per a simulation. Please clear the list if you want to add a different preset.")

#This is used add earth_sun_jupter into the list of bodies
def earth_sun_jupter_preset():
    error_label.config(text="")
    if len(list_of_all_bodies) == 0:
        list_of_all_bodies.extend(earth_sun_jupter)
        display_list()
    else:
        error_label.config(text="Sorry, can only add any preset once per a simulation. Please clear the list if you want to add a different preset.")


#Used to clear out the list of the bodies    
def clear_bodies():
    error_label.config(text="")
    list_of_all_bodies.clear()
    display_list()

#Used to calculate the total duration of the simulation
def cal_duration():
    years = float(duration.get())
    days = years *365

    # duration is a length of years split into seconds
    dur= days *24 *60 *60
    return dur

#This function is used for testing that the text box values are being taken in correctly
def show_body_values():
    error_label.config(text="")
    for x in range(len(list_of_all_bodies)):
        print ("This is body number: ",x + 1)
        print ("The mass of this body is: ", list_of_all_bodies[x].mass)
        print ("The X of this body is: ", list_of_all_bodies[x].x)
        print ("The Y of this body is: ", list_of_all_bodies[x].y)
        print ("The starting X velocity of this body is: ", list_of_all_bodies[x].x_velo)
        print ("The starting Y velocity of this body is: ", list_of_all_bodies[x].y_velo)

#This is used to turn the body into a string that will be used to display the information about the 
#body to the user        
def body_to_string(body):
    body_string = ""
    
    body_string += "The mass of this body is: " + str(body.mass) + "\n"
    body_string += "The X of this body is: " + str(body.x) + "\n"
    body_string += "The Y of this body is: " + str(body.y) + "\n"
    body_string += "The starting X velocity of this body is: " + str(body.x_velo) + "\n"
    body_string += "The starting Y velocity of this body is: " + str(body.y_velo) + "\n"
    body_string += "\n"
        
    return body_string
        
        
#This is using to create a body from the user inputs and place that into the list for holding
def add_body():
    try:
        error_label.config(text="")
        if float(size_of_body.get()) < 1000:
            error_label.config(text="Mass needs to be at least 1000")            
        else:           
            temp = b.body(float(size_of_body.get()), float(starting_x_body.get()), float(starting_y_body.get()), float(starting_xv_body.get()), float(starting_yv_body.get()))
            list_of_all_bodies.append(temp)
            display_list()
        
    except ValueError:
        error_label.config(text="Please make sure to only input numbers and not to leave any textboxes empty")

#This is used to display to the user all of the bodies that have been added into the simulation
def display_list():
    error_label.config(text="")
    temp = ""
    for x in list_of_all_bodies:
        temp += body_to_string(x)
        
    display_list_label.config(text=temp)
    
#This is used to rum the simualation by calling anum_orbit from Sim.py and inputing all of the list of bodys
#As well as all of the simulation values from the user    
def run_sim():
    error_label.config(text="")
    display_list()
    if len(list_of_all_bodies) != 0: 
        Sim.anim_orbit(list_of_all_bodies, cal_duration(), time_step.get(), speed_for_sim.get())
    else:
        error_label.config(text = "Must add bodies before running simulation")


#This is the set the mass of the body using a textbox
size_of_body_label = tk.Label(root, text="Mass of the body (Must be 1000 or greater)")
size_of_body = tk.Entry(root, width = 20)
size_of_body_label.grid(row=0, column=0)
size_of_body.grid(row=0, column=1)

#This is the set the starting x of the body using a textbox
starting_x_body_label = tk.Label(root, text="Starting X")
starting_x_body = tk.Entry(root, width = 20)
starting_x_body_label.grid(row=1, column=0)
starting_x_body.grid(row=1, column=1)

#This is the set the starting y of the body using a textbox
starting_y_body_label = tk.Label(root, text="Starting Y")
starting_y_body = tk.Entry(root, width = 20)
starting_y_body_label.grid(row=2, column=0)
starting_y_body.grid(row=2, column=1)

#This is the set the starting x velocity for body using a textbox
starting_xv_body_label = tk.Label(root, text="Starting X velocity")
starting_xv_body = tk.Entry(root, width = 20)
starting_xv_body_label.grid(row=3, column=0)
starting_xv_body.grid(row=3, column=1)

#This is the set the starting y velocity for the body using a textbox
starting_yv_body_label = tk.Label(root, text="Starting Y velocity")
starting_yv_body = tk.Entry(root, width = 20)
starting_yv_body_label.grid(row=4, column=0)
starting_yv_body.grid(row=4, column=1)

#This the textbox for the duration in years
duration_label = tk.Label(root, text="Enter the duration of the simulation (1 = one year, 2 = two year, etc...")
duration = tk.Entry(root, width = 20)
duration_label.grid(row=5, column=0)
duration.grid(row=5, column=1)

#add speed of sim radio buttons
speed_of_sim_label = tk.Label(root, text="Please select the speed of the simulation")
tk.Radiobutton(root, text = "normal", variable = speed_for_sim, value = "normal").grid(row=7, column=0)
tk.Radiobutton(root, text = "fast", variable = speed_for_sim, value = "fast").grid(row=7, column=1)
tk.Radiobutton(root, text = "very fast", variable = speed_for_sim, value = "vfast").grid(row=7, column=2)
tk.Radiobutton(root, text = "extremely fast", variable = speed_for_sim, value = "efast").grid(row=7, column=3)
speed_of_sim_label.grid(row=6, column=0)

#This allows the user to select the time step of the simulation
time_step_label = tk.Label(root, text = "Please select the time step")
tk.Radiobutton(root, text = "Hour", variable = time_step, value = 60*60).grid(row=9, column=0)
tk.Radiobutton(root, text = "Day", variable = time_step, value = 60 * 60 * 24).grid(row=9, column=1)
tk.Radiobutton(root, text = "Year", variable = time_step, value = 60 * 60 *24 * 365).grid(row=9, column=2)
time_step_label.grid(row=8, column=0)

#Add preset buttons right here
presets_here_label = tk.Label(root, text="Here are some presets")
presets_here_label.grid(row=10, column=0)

#-------------------------------------------------------------------------------------------------
#This is the present button for our solar system
our_solar_system = tk.Button(root, text="Our solar system preset", command=solar_preset)
our_solar_system.grid(row=11, column=0)

#This is the present button for our solar system with a black hole preset
our_solar_system_black_hole = tk.Button(root, text="Our solar system with a black hole preset", command=solar_preset_plus)
our_solar_system_black_hole.grid(row=11, column=1)

##This is the present button for earth and sun
earth_sun_button = tk.Button(root, text="Earth and Sun preset", command=earth_sun_preset)
earth_sun_button.grid(row=11, column=2)

##This is the present button for earth, sun, and jupter
our_solar_system_black_hole = tk.Button(root, text="Earth, Sun, and Jupter preset", command=earth_sun_jupter_preset)
our_solar_system_black_hole.grid(row=11, column=3)

#-------------------------------------------------------------------------------------------------

#This is the add button, to add the body to the list
add_body_button = tk.Button(root, text="Add body", command=add_body)
add_body_button.grid(row=15, column=0)

#This is the display bodies button,just used for the testing for now
display_bodies_button = tk.Button(root, text="Display Bodies", command=display_list)
display_bodies_button.grid(row=16, column=0)

#This is the run button
run_sim_button = tk.Button(root, text="Run Simulation", command=run_sim)
run_sim_button.grid(row=17, column=0)

#This is the button to clear the list of bodies
clear_bodies_button = tk.Button(root, text="Clear Bodies", command=clear_bodies)
clear_bodies_button.grid(row=18, column=0)

#This is will display each of the bodies than have been add into the list
display_list_label = tk.Label(root, text="")
display_list_label.grid(row=20, column=0)

#This will be used to show any errors to the user
error_label = tk.Label(root, text="")
error_space = tk.Label(root, text="        ")
error_label.grid(row=50, column=1)
error_space.grid(row=50, column=0)


root.mainloop()