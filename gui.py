from tkinter import *
import body as b

root = Tk()
root.title("Orbit Simulation")

#This is a temp holding places for the bodies that are created from the slider
list_of_all_bodies = []

#This is to hold the type of speed the sim will go by
speed_for_sim = StringVar()
speed_for_sim.set("normal")

#This function is used for testing that the silders values are being taken in correctly
def show_body_values():
    for x in range(len(list_of_all_bodies)):
        print ("This is body number: ",x + 1)
        print ("The mass of this body is: ", list_of_all_bodies[x].mass)
        print ("The X of this body is: ", list_of_all_bodies[x].x)
        print ("The Y of this body is: ", list_of_all_bodies[x].y)
        print ("The starting X velocity of this body is: ", list_of_all_bodies[x].x_velo)
        print ("The starting Y velocity of this body is: ", list_of_all_bodies[x].y_velo)
        
#This is using to create a body from the user inputs and place that into the list for holding
def add_body():
    temp = b.body(size_of_body.get(), starting_x_body.get(), starting_y_body.get(), starting_xv_body.get(), starting_yv_body.get())
    list_of_all_bodies.append(temp)

''' Using sliders would be nice since we will have full control of what the user would put into the model
It does also have some limitions like when it comes to selecting the correct number. I think we can have
the value of the slider be multiplied a certain number. 

'''


#This is the set the mass of the body using a slider
size_of_body_label = Label(root, text="Mass of the body")
size_of_body = Entry(root, width = 20)
size_of_body_label.grid(row=0, column=0)
size_of_body.grid(row=0, column=1)

#This is the set the starting x of the body using a slider
starting_x_body_label = Label(root, text="Starting X slider")
starting_x_body = Entry(root, width = 20)
starting_x_body_label.grid(row=1, column=0)
starting_x_body.grid(row=1, column=1)

#This is the set the starting y of the body using a slider
starting_y_body_label = Label(root, text="Starting Y slider")
starting_y_body = Entry(root, width = 20)
starting_y_body_label.grid(row=2, column=0)
starting_y_body.grid(row=2, column=1)

#This is the set the starting x velocity for body using a slider
starting_xv_body_label = Label(root, text="Starting X velocity slider")
starting_xv_body = Entry(root, width = 20)
starting_xv_body_label.grid(row=3, column=0)
starting_xv_body.grid(row=3, column=1)

#This is the set the starting y velocity for the body using a slider
starting_yv_body_label = Label(root, text="Starting Y velocity slider")
starting_yv_body = Entry(root, width = 20)
starting_yv_body_label.grid(row=4, column=0)
starting_yv_body.grid(row=4, column=1)

#add speed of sim slider
speed_of_sim_label = Label(root, text="Please select the speed of the simulation")
Radiobutton(root, text = "normal", variable = speed_for_sim, value = "normal").grid(row=6, column=0)
Radiobutton(root, text = "fast", variable = speed_for_sim, value = "fast").grid(row=6, column=1)
Radiobutton(root, text = "very fast", variable = speed_for_sim, value = "vfast").grid(row=6, column=2)
Radiobutton(root, text = "extremely fast", variable = speed_for_sim, value = "efast").grid(row=6, column=3)
speed_of_sim_label.grid(row=5, column=0)

#add slider for time step


#Add preset buttons right here


#This is the add button, to add the body to the list
add_body_button = Button(root, text="Add body", command=add_body)
add_body_button.grid(row=7, column=0)

#This is the display bodies button,just used for the testing for now
display_bodies_button = Button(root, text="Display Bodies", command=show_body_values)
display_bodies_button.grid(row=8, column=0)

#This is the run button, NOT CURRENTLY WORKING
run_sim_button = Button(root, text="Run Simulation", command=show_body_values)
run_sim_button.grid(row=9, column=0)


root.mainloop()