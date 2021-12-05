from tkinter import *
import body as b

root = Tk()
root.title("Orbit Simulation")

#This is a temp holding places for the bodies that are created from the slider
list_of_all_bodies = []


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
size_of_body = Scale(root, from_=2, to=10, orient=HORIZONTAL)
size_of_body_label.grid(row=0, column=0)
size_of_body.grid(row=0, column=1)

#This is the set the starting x of the body using a slider
starting_x_body_label = Label(root, text="Starting X slider")
starting_x_body = Scale(root, from_=2, to=10, orient=HORIZONTAL)
starting_x_body_label.grid(row=1, column=0)
starting_x_body.grid(row=1, column=1)

#This is the set the starting y of the body using a slider
starting_y_body_label = Label(root, text="Starting Y slider")
starting_y_body = Scale(root, from_=2, to=10, orient=HORIZONTAL)
starting_y_body_label.grid(row=2, column=0)
starting_y_body.grid(row=2, column=1)

#This is the set the starting x velocity for body using a slider
starting_xv_body_label = Label(root, text="Starting X velocity slider")
starting_xv_body = Scale(root, from_=2, to=10, orient=HORIZONTAL)
starting_xv_body_label.grid(row=3, column=0)
starting_xv_body.grid(row=3, column=1)

#This is the set the starting y velocity for the body using a slider
starting_yv_body_label = Label(root, text="Starting Y velocity slider")
starting_yv_body = Scale(root, from_=2, to=10, orient=HORIZONTAL)
starting_yv_body_label.grid(row=4, column=0)
starting_yv_body.grid(row=4, column=1)

#This is the add button, to add the body to the list
add_body_button = Button(root, text="Add body", command=add_body)
add_body_button.grid(row=5, column=0)

#This is the display bodies button,just used for the testing for now
display_bodies_button = Button(root, text="Display Bodies", command=show_body_values)
display_bodies_button.grid(row=6, column=0)

root.mainloop()