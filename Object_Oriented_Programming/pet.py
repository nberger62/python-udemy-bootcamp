class Pet:
    allowed=['cat', 'dog', 'fish', 'rat']
    def __int__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species

cat = Pet("Blue", "cat")
cat = Pet("Blue", "cat")
dog.species = "Tiger"



