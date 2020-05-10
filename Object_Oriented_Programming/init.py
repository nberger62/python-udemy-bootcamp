# _init_ method, use every time you make a new class. put space before _init_!!!!!

class User:
    def _init_(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
# self

user1 = User("Joe", "Smith", 40)
user2 = User("Nathan", "Berger", 25)
print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)