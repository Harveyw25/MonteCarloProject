from tree import *

MC = tree()
MC.expansion(MC.root)

timer = time.time() + 5

end = False

MC.printNode(MC.root)

while (not end) or (time.time() < timer):
    end = MC.cont()

MC.best()
