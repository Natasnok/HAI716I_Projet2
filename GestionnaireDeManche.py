class GestionnaireDeManche:
    def __init__(self, player1, player2, nbTours):
        self.p1 = player1
        self.p2 = player2
        self.nbTours = nbTours


    def manche(self):
        agent1Score = 0
        agent2Score = 0

        agent1CoupPrec = None
        agent2CoupPrec = None

        winner = None

        for i in range(self.nbTours):
            agent1Coup = self.p1.nextAction(agent2CoupPrec)
            agent2Coup = self.p2.nextAction(agent1CoupPrec)

            agent1CoupPrec = agent1Coup
            agent2CoupPrec = agent2Coup

            if agent1Coup == agent2Coup:
                if agent1Coup == "C": # C et C
                    agent1Score += 3
                    agent2Score += 3
                else:                 # D et D
                    agent1Score += 2
                    agent2Score += 2
            else:
                if agent1Coup == "C": # C et D
                    agent1Score += 0
                    agent2Score += 5
                else:                 # D et C
                    agent1Score += 5
                    agent2Score += 0

        if agent1Score > agent2Score:
            winner = "player1"
        elif agent1Score < agent2Score:
            winner = "player2"
        else:
            winner = "egalite"
        
        return winner