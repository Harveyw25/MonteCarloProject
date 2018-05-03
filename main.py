from tree import *
from game import *
from card import *

C = card("Card Name", 2, 1, 3)

newGame = game(4, [C, C, C], [C], [], 30, 30)

MC = tree(newGame)
MC.expansion(MC.root)

timer = time.time() + 5

end = False

MC.printNode(MC.root)

while (not end) or (time.time() < timer):
    end = MC.cont()

MC.best()
