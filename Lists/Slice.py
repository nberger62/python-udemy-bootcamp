#Slicing - make new lists using slices of the old list!
#some_list[start:end:step]

first_list = [1, 2, 3, 4]
print(first_list[2:])
#[3, 4]

#Don't forget the colon in the brackets

colors = ["red", "blue", "green","yellow","violet"]
print(colors[3:])
#['yellow', 'violet']

#where to start and end! basically the number before the colon and after
print(first_list[:2])
#[1, 2]

#Start and End Slice
print(first_list[1:3])
#[2, 3]

#Step of slice
first_list2 = [1, 2, 3, 4, 5, 6]
print(first_list2[1::2])
#[2, 4, 6]
print(first_list2[::2])
#[1, 3, 5]

#negative is going back
print(first_list2[1::-1])
#[2, 1]

#Tricks with Slices
string = "This is Fun!"
print(string[::-1])
#reversing a string /lists

