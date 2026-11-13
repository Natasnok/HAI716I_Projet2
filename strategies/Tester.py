from strategies.TitForTat import *

class Tester:
    def __init__(self):
        self.name = "Tester"

        self.actionAFaire = []
        self.TFT = False
    
    def nextAction(self, adverCoupPrec):
        if adverCoupPrec == 1:
            self.TFT = True

        if self.isFirstTurn(adverCoupPrec):
            self.actionAFaire = []
            self.TFT = False
            return 1 # D au premier tour
        elif self.TFT:
            return TitForTat.nextAction(self, adverCoupPrec)
        else:
            if self.actionAFaire == []:
                self.actionAFaire =[0,0,1]
            return self.actionAFaire.pop(0)

    def isFirstTurn(self, adverCoupPrec):
        if adverCoupPrec == None:
            return True
        return False
