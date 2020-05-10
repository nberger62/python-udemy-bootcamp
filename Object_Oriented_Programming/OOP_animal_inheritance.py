class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"this animal says {sound}")

class Cat(Animal):
    pass

blue = Cat()
blue.make_sound("MEOW")
print(blue.cool)
print(Cat.cool)

print(isinstance(blue, object))

# this animal says MEOW
# True
# True
# True
