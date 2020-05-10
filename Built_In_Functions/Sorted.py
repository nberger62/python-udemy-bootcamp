# sorted (works on anything that is iterable)

more_numbers = [6,1,8,2]
sorted(more_numbers)

users = [
    {"username": "Nate", "tweets": ["I love cake"]},
    {"username": "Sally", "tweets": ["I love pizza"]},
    {"username": "Chad", "tweets": ["I love bread"]},
    {"username": "Bill", "tweets": ["I love mysite"]},
]
print(sorted(users,key=lambda user: user['username'],reverse = True))

