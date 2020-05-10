class User:

    active users = 0

    def __init__(self, first, last, age):
        self.first=first
        self.last=last
        self.age=age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
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

# print(user1.likes("IceCream"))
# print(user2.likes("Chips"))

#print(user2.initials())
#print(user1.initials())
print(User.active_users)
