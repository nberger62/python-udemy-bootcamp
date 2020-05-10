class User:
    active_users = 0
# @classmethod! syntax for establishing a method below the class name, different than instance methods
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first,last,age = data_str.split(",")
        return cls(first,last,int(age))

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

class Moderator(User):
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community

    def remove_post(self):
        return f"{self.full_name()} removes a post from the {self.community} community"


print(User.display_active_users())
u1 = User("Tom", "Garcia", 35)
print(User.display_active_users())
jasmine = Moderator("Jasmine", "O'conner", 61, 'Piano')
print(User.display_active_users())

# There are currently 0 active users
# There are currently 1 active users
# There are currently 2 active users
