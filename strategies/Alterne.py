class Alterne:
    def __init__(self, rng, bruit):
        self.name = "Alterne"

        self.rng = rng
        self.bruit = bruit

        self.precedent = 1 # pour qu'il commence à C
    
    def nextAction(self, adverCoupPrec):
        nextAction = (1+self.precedent) % 2 # alterne entre C et D
        self.precedent = nextAction

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