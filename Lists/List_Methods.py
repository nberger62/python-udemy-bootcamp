#append - a list method in which it will add data to the end of the list

#ex - first_list = [1, 2, 3, 4]
#first_list.append(5)

#print(first_list) # [1, 2, 3, 4, 5]

data = [1, 2, 3]
data.append("blue")
print(data)

#extend will add to the end of a list all values

nums = [1,2,3]
len(nums)
nums.append([4,5])
len(nums)
nums.extend([4,5])
print(nums)

#So basically if you need to add one item, use append. If you are adding more than one item, use extend!

#insert - to inset an item in a certain position in the list
first_list = [1, 2, 3, 4]
first_list.insert(2,"Hi!")
print(first_list)

#clear - to remove items from the list all at once! gets rid of everything

first_list.clear()
print(first_list)

#pop - remove item at the given postion in the list, and return it - index number not value
second_list = [1, 2, 3, 4]
second_list.pop(0)
print(second_list)

#remove - removes first item from a list whose value is x, not index number

third_list = [1, 2, 3, 4]
third_list.remove(1)
print(third_list)

#index - find a specific item in a lsit, or where it occurs in the list. specify a start and end
numbers = [5, 6, 7, 8, 9, 10]
print(numbers.index(8))
#3

#count - retunrs the number of times x appears in the list, like the mode value in math... How many 2's are there?
numbers2 = [5, 6, 7, 8, 9, 10]
print(numbers2.count(5))
#1

#reverse - reverses the order of the list, doesn not make a new list or copy it, just reverses it
numbers3 = [1, 2, 3, 4, 5, 6]
numbers3.reverse()
print(numbers3)
#[6, 5, 4, 3, 2, 1]

#sort - sort the items in one place (list in place in ascending order)
another_list = [6, 4, 1, 2, 5]
another_list.sort()
print(another_list)
#[1, 2, 4, 5, 6]

#join - joins the list into one string
name = ["Nathan", "Berger"]
print(" ".join(name))
#Nathan Berger


