import math


class node:

    def __init__(self, game):
        self.name = ""
        self.game = game
        self.parent = None
        self.timesVisited = 0
        self.value = 0
        self.children = []
        self.selectionConstant = 2
        self.root = False
        self.dead = False

    def selectionScore(self, n):
        if self.timesVisited == 0:
            return math.inf
        else:
            return ((self.value/self.timesVisited)+(self.selectionConstant*(math.sqrt(math.log(n)/self.timesVisited))))

