#raise ValueError("hi")
#type
#name
#value
#syntax
# go to docs.python.org to check for all python errors and how to fix them

#We are going to display our own errors to other developers
def colorize(text, color):
    colors = ("cyan", "yellow", "blue")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")
colorize("hello", "red")
#colorize(34, "red")

#Traceback (most recent call last):
  #File "C:/Users/Nathan Berger/PycharmProjects/DEBUGGING/CommonErrors.py", line 12, in <module>
   # colorize("hello", "red")
  #File "C:/Users/Nathan Berger/PycharmProjects/DEBUGGING/CommonErrors.py", line 10, in colorize
   # raise ValueError("color is invalid color")
#ValueError: color is invalid color



