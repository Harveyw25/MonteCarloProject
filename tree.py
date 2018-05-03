from node import *
from game import *
import random
import time

class tree:
    root = node()
    root.root = True
    root.timesVisited = 1
    root.name += "1"


    def printNode(self, node):
        print("Name:", node.name, "Visited:", node.timesVisited, "Value:", node.value, "Children", len(node.children))
    
    def selection(self):
        temp = self.root
        
        while temp.timesVisited != 0 or temp == self.root:
            checker = temp
            
            for x in range(0, len(temp.children)):
                if temp.children[x].selectionScore(self.root.timesVisited) > temp.children[0].selectionScore(self.root.timesVisited):
                    temp.children.insert(0, temp.children.pop(x))

            for x in temp.children:
                if x.timesVisited == 0:
                    return x

            for x in temp.children:        
                if len(x.children) != 0 and not x.dead:
                    temp = x
                    break
                
            if checker == temp:
                temp.dead = True
                return 0

        

    def expansion(self, Node):
        actions = random.randint(0, 2)
        for x in range(0, actions):
            nodeToAdd = node()
            nodeToAdd.parent = Node
            nodeToAdd.name = nodeToAdd.parent.name + "-" + str(x)
            Node.children.append(nodeToAdd)

    def simulation(self, Node):
        Node.value = random.randint(0, 20)


    def backprop(self, n):
        temp = n

        valueToAdd = n.value
        
        times = temp.timesVisited
        temp.timesVisited = times + 1
        temp = temp.parent
        
        while temp.root == False:
            times = temp.timesVisited
            temp.timesVisited = times + 1
            temp.value = valueToAdd + temp.value
            temp = temp.parent

        times = temp.timesVisited
        temp.timesVisited = times + 1
        temp.value = valueToAdd + temp.value
        

    def cont(self):
        node = self.selection()
        
        if node != 0:
            
            self.simulation(node)
            self.expansion(node)
            self.backprop(node)
            self.printNode(node)
            return False
        else:
            return True

    def best(self):
        temp = self.root

        while len(temp.children) != 0:
            self.printNode(temp)

            for x in range(1, len(temp.children)):
                if temp.children[x].value > temp.children[0].value:
                    temp.children.insert(0, temp.children.pop(x))

            temp = temp.children[0]

        if temp.timesVisited != 0:
            self.printNode(temp)

            
    
        


