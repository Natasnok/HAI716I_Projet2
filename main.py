import sys
import random

from GestionnaireDeTournoi import GestionnaireDeTournoi

from strategies.ALLD import *
from strategies.Random import *
from strategies.TitForTat import *
from strategies.Joss import *
from strategies.Tester import *

from strategies.ALLC import *
from strategies.Alterne import *

matriceAxelrod = [
    [(3,3),(0,5)],
    [(5,0),(2,2)]
]

matriceChasseAuCerf = [
    [(4,4),(0,3)],
    [(3,0),(1,1)]
]

def main(argv):
    matrice = 0
    seed = None
    if len(argv) > 1:
        matrice = int(argv[1])
    if len(argv) > 2:
        seed = int(argv[2])
    
    
    if seed == None:
        seed = random.randint(100000, 999999)
    print(f"Seed de la partie : {seed}")
    rng = random.Random(seed)

    match matrice:
        case 0:
            matriceChosen = matriceAxelrod
            print("Matrice de la partie : Axelrod")
        case 1:
            matriceChosen = matriceChasseAuCerf
            print("Matrice de la partie : Chasse au cerf")
        case _:
            print("Matrice invalide. Choisissez 0 pour la matrice d'Axelrod ou 1 pour la matrice de chasse au cerf.")

    p1 = ALLD()
    p2 = Random(rng)
    p3 = TitForTat()
    p4 = Joss(rng)
    p5 = Tester()

    p6 = ALLC()
    p7 = Alterne()

    #joueurs = [p1,p2,p3,p4,p5]
    joueurs = [p1,p2,p3,p4,p5,p6,p7]

    gestTour = GestionnaireDeTournoi(joueurs,5,200,matriceChosen)
    gestTour.tournoi()


if __name__ == "__main__":
  main(sys.argv)