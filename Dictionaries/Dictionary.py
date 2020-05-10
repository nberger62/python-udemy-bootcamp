#Limitation of Lists not enough information, need more data of items in a list
#key values, pairs of data such as a label
#values is the actual data, think of it as indexes as the key values and the data is the string "blue"

cat = {"name": "blue", "age": 3.5, "isCute": True}
print(cat)

another_dictionary = dict(key = 'value')
print(another_dictionary)

#dict function can convert a data type, it is seperated by an equal sign ex - =

cat2 = dict(name="sally", age=0.5)
print(cat2)

#Dict EXC
user_info = dict(name="Nathan", age=25, ethnicity="white")
print(user_info)

#Individual Values

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


artist = {
    "first": "Neil",
    "last": "Young",
}

# concat first and last name with a space
full_name = artist["first"] + " " + artist["last"]
print(full_name)

#dictionary method and esting keys and values
#use the in for testing keys
"name" in instructor
"owns_dog" in instructor

#use in for testing values
"Colt" in instructor.values()

