class User:
    active_users = 0
# @classmethod! syntax for establishing a method below the class name, different than instance methods
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    def __init__(self, first, last, age):
        self.first=first
        self.last=last
        self.age=age
        User.active_users+=1

    def logout(self):
        User.active_users-=1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age+=1
        return f"Happy {self.age}th, {self.first}"

user1 = User("Joe", "Smith", 20)
user2 = User("Nathan", "Berger", 25)
print(User.display_active_users())
user1 = User("Joe", "Smith", 20)
user2 = User("Nathan", "Berger", 25)
print(User.display_active_users())

