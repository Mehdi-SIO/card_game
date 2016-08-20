from Carte import Carte
import random


class JeuCartes:
    def __init__(self):
        self.__cartes = []

        for val in range(2, 15):
            for coul in range(4):
                self.__cartes.append(Carte(val, coul))

    def __str__(self):
        carte_du_jeu = ""
        for carte in self.__cartes:
            if carte_du_jeu == "":
                carte_du_jeu = str(carte)
            else:
                carte_du_jeu += ", " + str(carte)
        return carte_du_jeu

    def melanger(self):
        return random.shuffle(self.__cartes)

    def tirer(self):
        try:
            return self.__cartes.pop(0)
        except IndexError as erreur:
            print("Il n'y a plus de cartes dans le jeu")
            return None