from GestionnaireDeTournoi import GestionnaireDeTournoi

from strategies.ALLD import *
from strategies.Random import *
from strategies.TitForTat import *
from strategies.Joss import *
from strategies.Tester import *

from strategies.ALLC import *
from strategies.Alterne import *

import random

matrice = [
    [(3,3),(0,5)],
    [(5,0),(2,2)]
]

def main(seed=None):
    if seed == None:
        seed = random.randint(100000, 999999)
    print(f"Seed de la partie : {seed}")
    rng = random.Random(seed)

    p1 = ALLD()
    p2 = Random(rng)
    p3 = TitForTat()
    p4 = Joss(rng)
    p5 = Tester()

    p6 = ALLC()
    p7 = Alterne()

    joueurs = [p1,p2,p3,p4,p5,p6,p7]

    gestTour = GestionnaireDeTournoi(joueurs,5,200,matrice)
    gestTour.tournoi()


if __name__ == "__main__":
    main(123456789)