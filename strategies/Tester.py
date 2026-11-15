from strategies.TitForTat import *

class Tester:
    def __init__(self, rng, bruit):
        self.name = "Tester"

        self.bruit = bruit
        self.rng = rng

        self.actionAFaire = []
        self.TFT = False
    
    def nextAction(self, adverCoupPrec):
        if adverCoupPrec == 1:
            self.TFT = True

        if self.isFirstTurn(adverCoupPrec):
            self.actionAFaire = []
            self.TFT = False
            nextAction = 1 # D au premier tour
        elif self.TFT:
            nextAction = TitForTat.nextAction(self, adverCoupPrec)
            return nextAction # le bruit est appliqué dans TitForTat
        else:
            if self.actionAFaire == []:
                self.actionAFaire =[0,0,1]
            nextAction = self.actionAFaire.pop(0)

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