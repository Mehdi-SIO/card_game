from JeuCartes import JeuCartes

if __name__ == "__main__":
    j = JeuCartes()
    j.melanger()
    print("On tire la première carte: ")
    print(j.tirer())