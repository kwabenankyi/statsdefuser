import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon

class Pitch:
    def __init__(self, topLeft, bottomRight, isoZone=100):
        self.topLeft = topLeft
        self.bottomRight = bottomRight
        self.isoZone = isoZone
        self.fig, self.ax = plt.subplots()

    def drawNewPitch(self):
        # Create a rectangle patch
        rect = patches.Rectangle((0,0), self.bottomRight[0], self.bottomRight[1], linewidth=2, edgecolor='g', facecolor='darkgreen')
        self.ax.add_patch(rect)


    def drawVisibleSegment(self, coords):
        tupleCoords = []
        for i in range (0, len(coords), 2):
            tupleCoords.append((coords[i], coords[i+1]))

        print(tupleCoords)
        visibleSegment = Polygon(tupleCoords, facecolor="green")
        self.ax.add_patch(visibleSegment)

    def drawPitch(self, coords):
        self.drawNewPitch()
        self.drawVisibleSegment(coords)
        self.ax.set_xlim([0, self.bottomRight[0]])
        self.ax.set_ylim([0, self.bottomRight[1]])
        self.ax.set_axis_off()
        self.fig.show()