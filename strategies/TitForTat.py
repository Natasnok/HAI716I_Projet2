class TitForTat:
    def __init__(self):
        self.name = "TitForTat"
    
    def nextAction(self, adverCoupPrec):
        if self.isFirstTurn(adverCoupPrec):
            return 0 # C au premier tour
        else:
            return adverCoupPrec # Coup passé de l'adversaire

    def isFirstTurn(self, adverCoupPrec):
        if adverCoupPrec == None:
            return True
        return False