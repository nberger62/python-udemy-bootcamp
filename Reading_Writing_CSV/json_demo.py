import json

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
c = Cat("Charles", "Tabby")

j = json.dumps(c.__dict__)

print(j)
