from GestionnaireDeManche import GestionnaireDeManche
from strategies.ALLD import ALLD

def main():
    p1 = ALLD()
    p2 = ALLD()
    m = GestionnaireDeManche(p1, p2, 200)
    print("Gagnant: ", m.manche())


if __name__ == "__main__":
    main()