class ALLD:
    def __init__(self):
        self.name = "ALLD"
    
    def nextAction(self, adverCoupPrec):
        return 1 # D

    def isFirstTurn(self, adverCoupPrec):
        if adverCoupPrec == None:
            return True
        return False
