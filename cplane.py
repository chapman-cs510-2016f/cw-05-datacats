#!/usr/bin/env python3

import abscplane


class ComplexPlane(abscplane.AbsComplexPlane):
    """ ComplexPlane is a class that 
    
    """
    def __init__(self, 
                 xmin = -10.0, xmax = 10.0, xlen = 20, ymin = -10.0, ymax = 10.0, ylen = 20, 
                 plane = [[]], f = lambda x : x):
        # initiate our initial values
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen
        self.ymax = xmax
        self.ymin = ymin
        self.ylen = ylen
        self.plane = plane
        self.f = f

        # call refresh to build our initial plane
        self.create_plane()

    def create_plane(self):
        # creating our initial variables:
        # creating an empty list, calculate our incremental values, start value, and end value
        xlist=[]
        inc_x = (abs(self.xmin)+abs(self.xmax))/self.xlen
        count = self.xmin
        stop = self.xmax
        # using a while loop, starting at our start value we increment by our inc x value and 
        # add that number to the end of the list. 
        while count <= stop
            xlist.append(count)
            count += inc_x

        # creating our initial variables:
        # creating an empty list, calculate our incremental values, start value, and end value
        ylist=[]
        inc_y = (abs(self.ymin)+abs(self.ymax))/self.ylen
        count = self.ymin
        stop = self.ymax
        # using a while loop, starting at our start value we increment by our inc x value and 
        # add that number to the end of the list.
        while count <= stop
            ylist.append(count)
            count += inc_y

        plane_list = xlist + 1j*ylist


    def refresh(self):

    def zoom(self):

    def set_f(self): 