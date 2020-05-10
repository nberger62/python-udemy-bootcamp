# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1, 2, 3, 4)

# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)

# 3 - Given the following variable:

values = [10,20,30]

# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)


# 4 - Given the following variable

stuff = [1,3,1,5,2,5,1,2,5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)

#Set Comprehension
print({x:x**2 for x in range(10)})
print({x**2 for x in range(10)})
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
#{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
#{char.upper() for char

string = "hello"
print({char for char in string if char in 'aeiou'})
print(len({char for char in string if char in 'aeiou'}))
#{'e', 'o'}
#2
