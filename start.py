from Carte import Carte

if __name__ == "__main__":

    c = Carte(12, 2)
    c2 = Carte(14, 3)

    print("Première carte:")
    print(c)

    print("\nDeuxième carte:")
    c2.affiche_ascii()