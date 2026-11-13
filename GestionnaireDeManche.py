class GestionnaireDeManche:
    def __init__(self, player1, player2, nbTours, matriceScore):
        self.p1 = player1
        self.p2 = player2
        self.nbTours = nbTours
        self.matriceScore = matriceScore


    def manche(self):
        agent1Score = 0
        agent2Score = 0

        agent1CoupPrec = None
        agent2CoupPrec = None

        for i in range(self.nbTours):
            agent1Coup = self.p1.nextAction(agent2CoupPrec)
            agent2Coup = self.p2.nextAction(agent1CoupPrec)

            agent1CoupPrec = agent1Coup
            agent2CoupPrec = agent2Coup

            resultat = self.matriceScore[agent1Coup][agent2Coup]
            agent1Score += resultat[0]
            agent2Score += resultat[1]
        
        return agent1Score,agent2Score