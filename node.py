import math

class node:
    parent = 0
    timesVisited = 0
    value = 0
    children = []
    selectionConstant = 2

    def selectionScore(self, n):
        if self.timesVisited == 0:
            return math.inf
        else:
            return ((self.value/self.timesVisited)+self.selectionConstant*(math.sqrt(math.log(n)/self.timesVisited)))

