import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Circle

class Pitch:
    def __init__(self, topLeft, bottomRight, isoZone=100, homeCol="red", awayCol="blue"):
        self.topLeft = topLeft
        self.bottomRight = bottomRight
        self.isoZone = isoZone
        self.fig, self.ax = plt.subplots()
        self.homeCol = homeCol
        self.awayCol = awayCol

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

    def drawPlayer(self, player):
        setColour = self.homeCol if player["teammate"] else self.awayCol
        if player["keeper"]:
            p = Circle(player["location"], radius=1, color="pink")
        else:
            p = Circle(player["location"], radius=1, color=setColour)
        if player["actor"]:
            p.set_linewidth(2)
            p.set_edgecolor("gold")
        self.ax.add_patch(p)

    def drawPlayers(self, players):
        for p in players:
            self.drawPlayer(p)
            self.fig.show()

    def drawPitch(self, coords, players):
        self.drawNewPitch()
        self.drawVisibleSegment(coords)
        self.drawPlayers(players)
        self.ax.set_xlim([0, self.bottomRight[0]])
        self.ax.set_ylim([0, self.bottomRight[1]])
        self.fig.show()