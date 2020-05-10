#Swapping values in a string or list
#shuffling a list of cards or sort through a list to find a custom sort, alg...

#List Comprehension
#the syntax
#[_for_in_]
#nums = [1, 2, 3]
#[x*10 for z in nums]

#Using list comprehensions:

#answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
#answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]

#Using good old manual loops:

answer = []
for person in ["Elie", "Tim", "Matt"]:
    print(answer.append(person[0]))
answer2 = ()
for num in [1,2,3,4,5,6]:
    if num % 2 == 0:
        print(answer2.append(num))

#Using list comprehensions(the more Pythonic way):

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

#Without list comprehensions, things are a bit longer:

answer = []
for x in [1,2,3,4]:
    if x in [3,4,5,6]:
        answer.append(x)
answer2 = []
for name in ["Elie", "Tim", "Matt"]:
    answer2.append(name[::-1].lower())

answer = [val for val in range(1,101) if val % 12 == 0]

SOLUTION
Using a string (preferable solution):

answer = [char for char in "amazing" if char not in "aeiou"]

Using a list:

answer = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]]

