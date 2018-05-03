from card import *

class game:

    def __init__(self, currentMana, cardsInHand, currentAllies, currentEnemies):
        self.hand = cardsInHand
        self.allies = currentAllies
        self.enemies = currentEnemies
        self.mana = currentMana

    def findActions(self)
        actionList = []

        for x in self.hand:
            if x.mana <= self.mana:
                
