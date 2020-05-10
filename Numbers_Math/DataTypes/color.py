color = "yellow"
if color == "blue":
    print("water")
elif color == "red":
    print("primary")
else:
    print("no color")

# NO TOUCHING ======================================
from random import choice

food = choice(['apple', 'grape', 'bacon', 'steak', 'worm'])
# NO TOUCHING ======================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if food == 'apple' or food == 'grape':
    print("fruit")
elif food == 'bacon' or food == 'steak':
    print("meat")
else:
    print("yuck")