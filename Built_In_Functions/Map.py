# a function that accepts at least two arguments... a function and an interable
#runs the lambda for each value

#1 = [1,2,3,4]

#doubles = list(map(lambda x: x*2, 1))

#evens # [2,4,6,8]

names = [
    {'first': 'Rusty', 'last': 'Steele'},
    {'first': 'Colt', 'last': 'Steele', },
    {'first': 'Blue', 'last': 'Steele', },
]

first_names = list(map(lambda x: x['first'], names))
print(first_names)

def decrement_list(l):
    return list(map(lambda n: n-1, l))