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

    def expansion(self, Node):
        actions = random.randint(1, 5)

        for x in range(0, actions+1):
            nodeToAdd = node()
            nodeToAdd.parent = node
            
            Node.children.append(nodeToAdd)

    def simulation(self, Node):
        Node.value = random.randint(-20, 20)

    def backprop(self, n):
        valueToAdd = n.value
        times = n.timesVisited
        n.timesVisited = times + 1 
        n = node.parent
        
        while(n != self.root):
            times = n.timesVisited
            n.timesVisited = times + 1
            n.value = valueToAdd + node.value

    def print(self, node):
        print(node.timesVisited, node.value)
        
MC = tree()

MC.expansion(MC.root)
Node = MC.selection()
MC.print(Node)
MC.simulation(Node)
MC.print(Node)
MC.backprop(Node)

MC.print(MC.root)

