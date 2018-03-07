import math

class node:

    def __init__(self):
        self.name = ""
        self.parent = None
        self.timesVisited = 0
        self.value = 0
        self.children = []
        self.selectionConstant = 2
        self.root = False

    def selectionScore(self, n):
        if self.timesVisited == 0:
            return math.inf
        elif n == 999999999:
            return -99999999999999999
        else:
            return ((self.value/self.timesVisited)+self.selectionConstant*(math.sqrt(math.log(n)/self.timesVisited)))

