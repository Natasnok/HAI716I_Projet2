from strategies.TitForTat import *

class InverseTitForTat:
    def __init__(self, rng, bruit):
        self.name = "InverseTitForTat"

        self.rng = rng
        self.bruit = bruit

    def nextAction(self, adverCoupPrec):
        nextAction = TitForTat.nextAction(self, adverCoupPrec) # imite TitforTat
        if nextAction == 0: # inverse l'action
            nextAction = 1
        else:
            nextAction = 0

        nextAction = self.bruitInverse(self.rng, nextAction, self.bruit)
        return nextAction

    def isFirstTurn(self, adverCoupPrec):
        if adverCoupPrec == None:
            return True
        return False

    def bruitInverse(self, rng, action, bruit):
        if rng.randint(1,100) <= bruit: # bruit fois sur 100
            if action == 0:
                return 1
            else:
                return 0
        return action