class Alterne:
    def __init__(self):
        self.name = "Alterne"

        self.precedent = 1 # pour qu'il commence à C
    
    def nextAction(self, adverCoupPrec):
        nextAction = (1+self.precedent) % 2 # alterne entre C et D
        self.precedent = nextAction
        return nextAction

    def isFirstTurn(self, adverCoupPrec):
        if adverCoupPrec == None:
            return True
        return False