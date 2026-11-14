from GestionnaireDeManche import GestionnaireDeManche

class GestionnaireDeTournoi:
    def __init__(self, joueurs, nbPartie, nbManche, matrice):
        self.joueurs = joueurs
        self.nbPartie = nbPartie
        self.nbManche = nbManche
        self.matrice = matrice

        self.scoreJoueursTournoi = [0 for i in range(len(joueurs))]


    def tournoi(self):
        nbJoueurs = len(self.joueurs)
        for i in range(nbJoueurs-1):
            for j in range(i+1,nbJoueurs):
                p1 = self.joueurs[i]
                p2 = self.joueurs[j]
                p1score, p2score = 0,0
                for p in range(self.nbPartie):
                    gestMan = GestionnaireDeManche(p1, p2, self.nbManche, self.matrice)
                    scoreManche = gestMan.manche()
                    p1score += scoreManche[0]
                    p2score += scoreManche[1]

                if p1score > p2score:
                    print(p1.name, "gagne contre", p2.name,"(", p1score,"à", p2score,"). En", self.nbPartie, "parties de", self.nbManche, "manches.")
                    print(p1.name, "gagne 2 points pour le tournoi !")
                    self.scoreJoueursTournoi[i] += 2
                elif p1score < p2score:
                    print(p2.name, "gagne contre", p1.name,"(", p2score,"à", p1score,"). En", self.nbPartie, "parties de", self.nbManche, "manches.")
                    print(p2.name, "gagne 2 points pour le tournoi !")
                    self.scoreJoueursTournoi[j] += 2
                else:
                    print("Egalité entre",p1.name,"et",p2.name,"même score de", p1score, ". En", self.nbPartie, "parties de", self.nbManche, "manches.")
                    print("Les deux joueurs gagnent 1 point chaqu'un pour le tournoi !")
                    self.scoreJoueursTournoi[i] += 1
                    self.scoreJoueursTournoi[j] += 1
                print("")

        self.classement()

    def classement(self):
        classement = []

        for i in range(len(self.joueurs)):
            classement.append((self.joueurs[i].name, self.scoreJoueursTournoi[i]))

        classement.sort(key=lambda x: x[1], reverse=True)

        print("\n========== CLASSEMENT DU TOURNOI ==========")
        for i, (nom, score) in enumerate(classement):
            print(i + 1, "-", nom, ":", score, "points")
        print("===========================================")


