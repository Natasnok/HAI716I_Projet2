class TitForTat:
    def __init__(self, rng, bruit):
        self.name = "TitForTat"

        self.rng = rng
        self.bruit = bruit

    def nextAction(self, adverCoupPrec):
        if self.isFirstTurn(adverCoupPrec):
            nextAction =  0 # C au premier tour
        else:
            nextAction = adverCoupPrec # Coup passé de l'adversaire

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