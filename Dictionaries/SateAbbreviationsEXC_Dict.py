list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = dict(zip(list1,list2))
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer2 = dict(person)
print(answer2)

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {}.fromkeys("aeiou", 0)

answer3 = {count: chr(count) for count in range(65,91)}
print(answer3)
