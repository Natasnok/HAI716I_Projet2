from strategies.TitForTat import *

class Joss:
    def __init__(self, rng):
        self.name = "Joss"

        self.rng = rng
    
    def nextAction(self, adverCoupPrec):
        nextAction = TitForTat.nextAction(self, adverCoupPrec) # imite TitforTat
        if nextAction == 0: # si C
            if self.rng.randint(0, 9) == 0: # 1 fois sur 10
                return 1 # D
        
        return nextAction
            

    def isFirstTurn(self, adverCoupPrec):
        if adverCoupPrec == None:
            return True
        return False