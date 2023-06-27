"""
Animation:
This code creates a submarine that moves up and down while changing color.
The submarine will move to where the mouse is clicked.

File Name: howry_project_4.py
Author: Serena Strawn (Function) & Ken Howry (Animation)
Date: 22.10.9
Course: COMP 1351
Assignment: Project IV
Collaborators: N/A
Internet Source: N/A
"""


from random import randint

import dudraw

#setting canvas size
dudraw.set_canvas_size(500, 500)

#submarine drawing
def submarine (x:float, y:float, w:float, h:float)->None:
        """
            The submarine function draws a submarine of random color. The lower left corner is the origin for the parameters and is the lower left corner of the sumbarine. 
            parameters: 
                x:float is the x position of the submarine with zero on the left side of the window
                y:float is the y position of hte submarien with zero on the bottom side fo the window
                w:float is the width of the submarine
                y:float is the height of the submarine
            return: None
        """
        #set random pen color
        color1 = randint(0,255)
        color2 = randint(0,255)
        color3 = randint(0,255)

        dudraw.set_pen_color_rgb(color1, color2, color3)
        #body
        dudraw.filled_ellipse (0.2*w+x, 0.1*h+y, 0.2*w, 0.1*h)
        #body end
        dudraw.filled_quadrilateral(0.25*w+x, 0*h+y, 0.25*w+x, 0.2*h+y, 0.5*w+x, 0.15*h+y, 0.5*w+x, 0.05*h+y)
        #propellor
        dudraw.filled_rectangle(0.55*w+x, 0.1*h+y, 0.05*w, 0.01*h)#spoke
        dudraw.filled_rectangle(0.6*w+x, 0.1*h+y, 0.01*w, 0.05*h)#spoke end
        dudraw.filled_triangle(0.6*w+x, 0.14*h+y, 0.59*w+x, 0.2*h+y, 0.61*w+x, 0.2*h+y)#top paddle
        dudraw.filled_triangle(0.6*w+x, 0.06*h+y, 0.59*w+x, 0.0*h+y, 0.61*w+x, 0.0*h+y)#bottom paddle
        #fins
        dudraw.filled_quadrilateral(0.45*w+x, 0.13*h+y, 0.47*w+x, 0.19*h+y, 0.52*w+x, 0.2*h+y, 0.52*w+x, 0.13*h+y)#top fin
        dudraw.filled_quadrilateral(0.45*w+x, 0.07*h+y, 0.47*w+x, 0.01*h+y, 0.52*w+x, 0.0*h+y, 0.52*w+x, 0.07*h+y)#bottom fin
        #top bunker
        dudraw.filled_rectangle(0.2*w+x, 0.2*h+y, 0.06*w, 0.05*h)
        #periscope
        dudraw.filled_rectangle(0.2*w+x, 0.3*h+y, 0.015*w, 0.05*h)#vertical piece
        dudraw.filled_rectangle(0.165*w+x, 0.36*h+y, 0.05*w, 0.013*h)#horizontal piece
        dudraw.filled_rectangle(0.115*w+x, 0.36*h+y, 0.01*w, 0.02*h)#end piece
        #windows
        dudraw.set_pen_color_rgb(41, 41, 41)
        dudraw.filled_ellipse(0.15*w+x, 0.1*h+y, 0.03*w, 0.03*h)
        dudraw.filled_ellipse(0.25*w+x, 0.1*h+y, 0.03*w, 0.03*h)
        dudraw.filled_ellipse(0.35*w+x, 0.1*h+y, 0.03*w, 0.03*h)

#variables for location and movement
x_loc_1 = 0.5
y_velocity_1 = 0.05
y_loc_1  = 0.05

while True:
    dudraw.clear_rgb (52, 149, 235)
    submarine(x_loc_1, y_loc_1, 0.8, 0.8)

    #moving the object by changing y_loc_1
    y_loc_1 += y_velocity_1

    if dudraw.mouse_pressed():
        #move the submarine to the mouse location
        x_loc_1= dudraw.mouse_x()
        y_loc_1 = dudraw.mouse_y()

    #check collision with boundary
    if y_loc_1 > 0.8 or y_loc_1 < 0:
        #reverse direction by changing the velocity sign
        y_velocity_1 *= -1

    dudraw.show(60)
