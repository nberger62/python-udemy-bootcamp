def be_polite(fn):
    def wrapper():
        print("Nice to meet you!")
        fn()
        print("Have a shitty day!")
    return wrapper

@be_polite
def greet():
    print("My name is Fucking BATMAN!!!!!!!!!")

greet()

# Nice to meet you!
# My name is Fucking BATMAN!!!!!!!!!
# Have a shitty day!

def my_decorator(fn):
    def wrapper(*args, **kwargs):
        # do so stuff
        pass
    return wrapper