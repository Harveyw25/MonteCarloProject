from node import *
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
        highestScore = node()
        highestScore.timesVisited = 999999999
        temp = self.root

        i = 0
        
        while temp.timesVisited != 0:
            
            for x in temp.children:
                highestScore = node()
                highestScore.timesVisited = 999999999
                print("comparing", x.name, highestScore.name)
                if x.selectionScore(self.root.timesVisited) > highestScore.selectionScore(self.root.timesVisited):
                    highestScore = x
                    #print(x.name, "Wins")
            temp = highestScore
            i += 1
            if temp.timesVisited == 999999999 or i == 1000:
                return 0

        return temp

    def expansion(self, Node):
        actions = random.randint(0, 4)
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
    
        
MC = tree()
MC.expansion(MC.root)

timer = time.time() + 5

end = False

MC.printNode(MC.root)

while (not end) or (time.time() < timer):
    end = MC.cont()    

