class ALLC:
    def __init__(self):
        self.name = "ALLC"
    
    def nextAction(self, adverCoupPrec):
        return 0 # C

    def isFirstTurn(self, adverCoupPrec):
        if adverCoupPrec == None:
            return True
        return False