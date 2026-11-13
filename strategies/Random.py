class Random:
    def __init__(self, rng):
        self.name = "Random"

        self.rng = rng
    
    def nextAction(self, adverCoupPrec):
        return self.rng.randint(0, 1) # C ou D

    def isFirstTurn(self, adverCoupPrec):
        if adverCoupPrec == None:
            return True
        return False