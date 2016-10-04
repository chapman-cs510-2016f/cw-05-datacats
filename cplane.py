#!/usr/bin/env python3

import abscplane

"""Complex Plane Creation
This module imports from the class abscplane, and inherits the class' object
and variables.
This module expands on the class by creating a complex number plane,
creating a 2 dimensional grid of complex numbers in the form of (x + y * 1j)
where 1j is the imaginary untit, defined in mathematics as i; the square root of -1.
The exect specifications of the grid is left to the user.
The class as attributes of the following:
        xmax (float) : maximum horizontal axis value
        xmin (float) : minimum horizontal axis value
        xlen (int)   : number of horizontal points
        ymax (float) : maximum vertical axis value
        ymin (float) : minimum vertical axis value
        ylen (int)   : number of vertical points
        plane        : stored complex plane implementation
        f    (func)  : function displayed in the plane


This module also has 3 aditional functions that are used to transform the 2d grid as needed.:
    refresh : redraws the plane creation
    zoom    : resets graph's x and y values to "zoom in/out", and redraws the graph with new perameters
    set_f   : resets the transformation function for the graph, then redraws the graph.
More information on how to use each function is located in the functions' docstring.

"""


class ComplexPlane(abscplane.AbsComplexPlane):
    """Complex Plane Class: Sets the initial values for the object, as well as creates the plane.

         The creation takes in the following arugments, and has default values if no value is passed through:

            param1 (float) : minimum horizontal, X, axis value. Default value of -10
            param2 (float) : maximum horizontal, X, axis value. Default value of 10
            param3 (int)   : number of horizontal points between the x-min and x-max values. Default value of 20.
            param4 (float) : maximum vertical, Y, axis value. Default value of 10
            param5 (float) : minimum vertical, Y, axis value. Default value of -10
            param6 (int)   : number of vertical points between the y-min and y-max values. Default value of 20
            param7         : stored complex plane implementation. Defaulted as a black list, []
            param8 (func)  : function displayed in the plane. Default function as the identity function. x:x

        The initialization will also call the class function, create_plane() to create the plane with the given
        arugments.
    """

    def __init__(self, xmin=-10.0, xmax=10.0, xlen=20, ymin=-10.0, ymax=10.0, ylen=20, plane=[], f=lambda x:x):
        # initiate our initial values
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen
        self.ymin = xmin
        self.ymax = ymax
        self.ylen = ylen
        self.plane = plane
        self.f = f

        # call refresh to build our initial plane
        self.create_plane()

    def create_plane(self):
        """Create Plane
        Creation of the plane.
        This function will take the set values of xmin, xmax, xlen, ymin, ymax, ylen to
        create the plane.
        It will also take the set value of f and apply the function upon creation of the plane values
        and stores all values as lists within the class' plane variable.

        """
        # First we calculate our point increment for both the x and y values
        inc_x = (abs(self.xmin)+abs(self.xmax))/self.xlen
        inc_y = (abs(self.ymin)+abs(self.ymax))/self.ylen

        # This for-loop will add every x-value with every y-value, saving the values column wise
        # i.e. (-10,-10), (-10,-9), (-10.-8),...,(-10,n) for n = our y-values.
        # store these combinations into a list, and add that to our plane. 
        # The nested loop will then traverse again and will get the combinations for the next x-value.
        # The loop will continue until all x-values and y-value combinations are added to our plane.
        for y in range(0, self.ylen + 1):
            temp_list = []
            for x in range(0, self.xlen + 1):
                temp_list.append(self.f((self.xmin + x*inc_x) + (self.ymin + y*inc_y)*1j))
            self.plane.append(temp_list)

    def refresh(self):
        """Regenerate complex plane.
        For every point (x + y*1j) in the plane, replace
        the point with the value self.f(x + y*1j).
        The function will first delete the existing plane and redraw the plane again
        by calling the create_plane() function. 
        """

        # delete the existing plane first before recreating our plane.
        self.plane = []

        # calling our create_plane() to redraw our plane.
        self.create_plane()

    def zoom(self, xmin, xmax, xlen, ymin, ymax, ylen):
        """This function zooms into the graph, given by the parameters
        Args:
            param1 (float) : The new value for the minimum horizontal axis
            param2 (float) : The new value for the maximum horizontal axis
            param3 (int)   : The new value for the horizontal points between the x-max and x-min values.
            param4 (float) : The new value for the maximum horizontal axis
            param5 (float) : The new value for the minimum horizontal axis
            param6 (int)   : mThe new value for the vertical points between the y-max and y-min values.

        This function takes in a user input of xmin, xmax, xlen, ymin, ymax, ylen and resets
        the class values to the parameters.
        The function will then 'zoom in' by recreating the graph, given the newly defined values
        by calling the refresh() function.
        """
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen
        self.ymin = ymin
        self.ymax = ymax
        self.ylen = ylen
        self.refresh()

    def set_f(self, f):
        """This function applies a new function to be applied to the grid's values and recreates the grid
        Args:
            param1 (function)  : a new function to be passed onto the grid.

        This function sets a new value to the class' function variable with the given parameter and then
        recreates the grid by calling the refresh() function.
        """
        self.f = f
        self.refresh()



