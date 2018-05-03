from card import *
from node import *
from tree import *

class game:

    def __init__(self, mana, hand, allies, enemies, allyHealth, enemyHealth):
        self.hand = hand
        self.allies = allies
        self.enemies = enemies
        self.mana = mana
        self.allyHealth = allyHealth
        self.enemyHealth = enemyHealth
    
    def findActions(self, Node):
        #attacking
        for x in range(0, len(self.allies)):
            if(self.allies[x].ableToAttack):
                self.allies[x].ableToAttack = False
                newGame = game(self.mana, self.hand, self.allies, self.enemies, self.allyHealth, self.enemyHealth - self.allies[x].attack)
                newNode = node(newGame)
                newNode.parent = Node
                newNode.name = "Attack " + self.allies[x].name + " into enemy hero"
                Node.children.append(newNode)
            
                for y in range(0, len(self.enemies)):
                    newGame = game(self.mana, self.hand, list(self.allies), list(self.enemies), self.allyHealth, self.enemyHealth)
                    newGame.allies[x].health -= newGame.enemies[y].attack
                    newGame.enemies[y].health -= newGame.allies[x].attack
                    
                    if newGame.allies[x].health <= 0:
                        newGame.allies.pop(x)
                    if newGame.enemies[y].health <= 0:
                        newGame.enemies.pop(y)

                    newNode = node(newGame)
                    newNode.parent = Node
                    newNode.name = "Attack " + self.allies[x].name + " into " + self.enemies[y].name
                    Node.children.append(newNode)

        #playing from hand
        for x in range(0, len(self.hand)):
            if self.hand[x].mana <= self.mana:
                newGame = game(self.mana - self.hand[x].mana, list(self.hand), list(self.allies), self.enemies, self.allyHealth, self.enemyHealth)
                newGame.hand[x].ableToAttack = False
                newGame.hand.pop(x)
                newGame.allies.append(self.hand[x])
                newNode = node(newGame)
                newNode.parent = Node
                newNode.name = "Play " + self.hand[x].name
                Node.children.append(newNode)

    def simAction(self, Node):
        value = self.allyHealth - self.enemyHealth

        if self.allyHealth <= 0:
            value = -100000

        if self.enemyHealth <= 0:
            value = 100000

        for x in self.allies:
            value += x.attack
            value += x.health

        for x in self.enemies:
            value -= x.attack
            value -= x.health

        return value
