from tkinter import * 
from tkinter.ttk import * 

class PitchDrawing:
    def __init__(self, master, topLeft, bottomRight, isoZone):
        self.master = master if master else None
        self.topLeft = topLeft
        self.bottomRight = bottomRight
        self.isoZone = isoZone
        self.create()
     
    def create(self):
        self.canvas = Canvas(self.master)
        # Creates a rectangle of 50x60 (heightxwidth)
        self.canvas.create_rectangle(self.isoZone + self.topLeft[0],
                                     self.isoZone + self.topLeft[1], 
                                     self.isoZone + self.bottomRight[0]*5, 
                                     self.isoZone + self.bottomRight[1]*5,
                                outline = "black", fill = "darkgreen",
                                width = 2)
         
        # Pack the canvas to the main window and make it expandable
        self.canvas.pack(fill = BOTH, expand = 1)
 

def drawNewPitch(name, topLeft, bottomRight, isoZone = 100):
    master = Tk()
    master.title = name
    master.geometry(f"{bottomRight[0]*5+isoZone*2}x{bottomRight[1]*5+isoZone*2}")
    pitchDraw = PitchDrawing(master, topLeft, bottomRight, isoZone)
    master.mainloop()


drawNewPitch("pitch",[0,0],[120,80])