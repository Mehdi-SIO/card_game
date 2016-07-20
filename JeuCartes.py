from Carte import Carte

class JeuCartes:
    def __init__(self):
        self.cartes = []

        for val in range(2, 15):
            for coul in range (4):
                self.cartes.append(Carte(val, coul))