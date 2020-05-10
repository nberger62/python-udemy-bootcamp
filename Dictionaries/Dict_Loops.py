instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"}
print(instructor["name"])
#Colt

#forloops
for value in instructor.values():
    print(value)
#forloops in dict.s for values or left column
for keys in instructor.keys():
    print(keys)
#for loops for values in right column

#BOTH!!!!!!!!!!!!!!!!!!!!!!!
for key,value in instructor.items():
    print(key,value)
    break