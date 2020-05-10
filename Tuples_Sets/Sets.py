#lighterweight than a dict or lists
#like formal math
#like sets of data that do not have duplicate sets of data and they are not ordered
#you cannot use index for sets
s = set({1, 4, 5})
print(s)
#{1, 4, 5}
p = set({1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 7})
print(p)
#{1, 2, 3, 4, 5, 6, 7} no duplicates!

#SET Methods
#add
s.add(8)
print(s)
#{8, 1, 4, 5}

#remove
s.remove(1)
print(s)
#{8, 4, 5}

#clear
s.clear()
#clears all

#copy s.copy

#Set Math
#intersection
#different
#unique entry sets
