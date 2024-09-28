import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle

class Pitch:
    def __init__(self, topLeft, bottomRight, isoZone=100, homeCol="red", awayCol="blue"):
        self.topLeft = topLeft
        self.bottomRight = bottomRight
        self.isoZone = isoZone
        self.fig, self.ax = plt.subplots()
        self.homeCol = homeCol
        self.awayCol = awayCol

    def drawNewPitch(self, coords):
        # Create a rectangle patch
        rect = Rectangle((0,0), self.bottomRight[0], self.bottomRight[1], linewidth=2, edgecolor='g', facecolor='darkgreen')
        self.ax.add_patch(rect)

        self.drawVisibleSegment(coords)
        self.drawPitchMarkings()

    def drawVisibleSegment(self, coords):
        tupleCoords = []
        for i in range (0, len(coords), 2):
            tupleCoords.append((coords[i], coords[i+1]))

        visibleSegment = Polygon(tupleCoords, facecolor="green")
        self.ax.add_patch(visibleSegment)

    def drawPitchMarkings(self):
        outside_rect = Rectangle((0,0), self.bottomRight[0], self.bottomRight[1], linewidth=2, edgecolor='white', facecolor='none')
        centre_circle = Circle((self.bottomRight[0]/2, self.bottomRight[1]/2), linewidth=2, radius=9.15, edgecolor="white", facecolor="none")
        box_18_1 = Rectangle((0,self.bottomRight[1]/2-20.16), 16.5, 40.32, linewidth=2, edgecolor='white', facecolor='none')
        box_18_2 = Rectangle((self.bottomRight[0]-16.5,self.bottomRight[1]/2-20.16), 16.5, 40.32, linewidth=2, edgecolor='white', facecolor='none')
        box_6_1 = Rectangle((0,self.bottomRight[1]/2-9.16), 5.5, 18.32, linewidth=2, edgecolor='white', facecolor='none')
        box_6_2 = Rectangle((self.bottomRight[0]-5.5,self.bottomRight[1]/2-9.16), 5.5, 18.32, linewidth=2, edgecolor='white', facecolor='none')
        pen_spot_1 = Circle((11, self.bottomRight[1]/2), radius=0.5, color="white")
        pen_spot_2 = Circle((self.bottomRight[0]-11, self.bottomRight[1]/2), radius=0.5, color="white")
        halfway = Rectangle((self.bottomRight[0]/2-0.5, 0), 1, self.bottomRight[1], linewidth=0, color="white")

        self.ax.add_patch(outside_rect)
        self.ax.add_patch(centre_circle)
        self.ax.add_patch(box_18_1)
        self.ax.add_patch(box_18_2)
        self.ax.add_patch(box_6_1)
        self.ax.add_patch(box_6_2)
        self.ax.add_patch(pen_spot_1)
        self.ax.add_patch(pen_spot_2)
        self.ax.add_patch(halfway)

    def drawPlayer(self, player):
        setColour = self.homeCol if player["teammate"] else self.awayCol
        if player["keeper"]:
            if player["teammate"]:
                p = Circle(player["location"], radius=1, color="orange")
            else:
                p = Circle(player["location"], radius=1, color="black")
        else:
            p = Circle(player["location"], radius=1, color=setColour)
        if player["actor"]:
            p.set_linewidth(2)
            p.set_edgecolor("gold")
        self.ax.add_patch(p)

    def drawPlayers(self, players):
        for p in players:
            self.drawPlayer(p)

    def drawPitch(self, coords, players):
        self.drawNewPitch(coords)
        self.drawPlayers(players)
        self.ax.set_xlim([0, self.bottomRight[0]])
        self.ax.set_ylim([0, self.bottomRight[1]])