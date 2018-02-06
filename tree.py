from node import *
import random

class tree:
    root = node()

    def selection(self):
        highestScore = node()
        highestScore.timesVisited = math.inf
        temp = self.root

        while temp.timesVisited != 0:
            for x in temp.children:
                if x.selectionScore(self.root.timesVisited) > highestScore.selectionScore(self.root.timesVisited):
                    highestScore = x
            temp = x
            
        return temp

    def expansion(node):
        actions = random.randint(1, 5)

        for x in range(0, actions+1):
            nodeToAdd = node()
            nodeToAdd.parent = node
            
            node.children.append(nodeToAdd)
    
