# *args a special operator we can pass to functions. Gathers remaining arguments as a tuple

#this is just a tuple etc...

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num,
    return total

print(sum_all_nums(4,6,9,4,10))
print(sum_all_nums(4,6))

#parameter ordering
#1 parameters
#2 *args
#3 default parameters
#**kwargs
#print the first result with the nubers 1, 4, 7. Then print all the numbers.
# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1,4,7)
result2 = count_sevens(*nums)
