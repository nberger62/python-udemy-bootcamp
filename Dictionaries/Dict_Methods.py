instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"}

#clear - clears all keys and values in a dictionary
instructor.clear()
print(instructor)
#{}

instructor2 = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"}

#copy - makes a copy
#c = d.copy
#clone = d.copy
instructor2.copy()
print(instructor2)

#fromkeys - creates key-values pairs from comma seperated values
#{}.fromkeys("a" , "b")
#new_user = {}.fromkeys([])
#new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio': 'unknown'])

#get - retrieves a key in an object and return NONE instead of a keyerror if the key does not exist:
print(instructor2.get('name'))
#Colt

#pop - removes a single item, just like in lists, but you have to provide the key for the key value pair
print(instructor2.pop("owns_dog"))

#update - take a lsit and update the values into another key or list
#second.update(first)

instructor3 = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"}

person = {"city": "Antigua"}
person.update(instructor3)
print(instructor3)

