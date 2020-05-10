class Chicken:
    total_eggs = 0
    def __int__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        self.eggs+=1
        Chicken.total_eggs+=1
        return self.eggs

c1 = Chicken(name="Alice", species="Partridge Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")

print(c1.lay_egg())
