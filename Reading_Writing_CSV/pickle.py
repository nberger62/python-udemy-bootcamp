with open("pets.pickle", "rb") as file:
    zombie_blue = pickle.load(file)
    print(zombie_blue)
    print(zombie_blue.play())
    