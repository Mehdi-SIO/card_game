class Carte:
    valeurs = (None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As")
    couleurs = ("Coeur", "Carreau", "Trèfle", "Pique")

    def __init__(self, val, coul):
        if val < 2 or val > 14:
            print("Erreur: La valeur d'une carte est comprise entre 2 et 14")
            exit(1)
        if coul < 0 or coul > 3:
            print("Erreur: Le code couleur d'une carte est compris entre 0 et 3")
            exit(1)
        self.__valeur = val
        self.__couleur = coul

    def __str__(self):
        return str(Carte.valeurs[self.__valeur]) + " de " + Carte.couleurs[self.__couleur]

    def affiche_ascii(self):
        nom = str(Carte.valeurs[self.__valeur]) + " de " + Carte.couleurs[self.__couleur]
        taille = len(nom) + 2
        print("/", "-" * taille, "\\", sep="")
        print("|", "-" * taille, "|", sep="")
        print("|", nom,  "|")
        print("|", "-" * taille, "|", sep="")
        print("\\", "-" * taille, "/", sep="")

    def __getValeur(self):
        print("Passage dans getValeur")
        return self.__valeur

    def __setValeur(self, val):
        print("Passage dans setValeur")
        self.__valeur = val

    valeur = property(__getValeur, __setValeur)

    def __getCouleur(self):
        print("Passage dans getCouleur")
        return self.__couleur

    def __setCouleur(self, coul):
        print("Passage dans setCouleur")
        self.__couleur = coul

    couleur = property(__getCouleur, __setCouleur)


