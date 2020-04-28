#Ganesh Jainarain
#CSI 32
#March 27, 2019
#Rectangle Bullseye class

import tkinter as tk


class Bullseye:
    '''Class to draw Bullseye with alternating bands of black and white.


    This class takes as input, a canvas, the center of the canvas, number of bands, largest radius,
    and optional two band colors.'''
     
    def __init__(self, formalCanvas, cx,cy, numBands, radius, primary = 'black', secondary = 'white'):
        '''Constructor,'''
        
        if numBands <= 0:
            raise ValueError('Number of bands must be positive.')
        if radius <= 0:
            raise ValueError('Radius must be positive.') #Want the radius and number of bands to be positive.

        self.numBands = numBands
        self.radius = radius
        self.canvas = formalCanvas
        
        
        self.x1 = cx - self.radius
        self.y1 = cy - self.radius
        self.x2 = cx + self.radius
        self.y2 = cy + self.radius #Opposite vertices of rectangle bounding the circle.
        
        self._outer = self.canvas.create_rectangle(self.x1,self.y1, self.x2, self.y2, fill = primary)
                             #The outer circle
        if numBands == 1:
            self._rest = None
        else:
            innerRadius = float(radius)* (numBands -1)/numBands
            self._rest = Bullseye(self.canvas, cx, cy, numBands-1, innerRadius, secondary, primary)
                             #Recursion.    

def drawBullseye(num, radius,primary='black', secondary = 'white'):
    root = tk.Tk()
    size = 2*radius + 20
    canvas = tk.Canvas(root,width = size, height = size)
    canvas.pack()
    Bullseye(canvas, radius+10, radius+10, num, radius, primary, secondary)

    
