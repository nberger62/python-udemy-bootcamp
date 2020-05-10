max(3,67,99)
min(3,67,99)

names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]
min(names)
max(names)
min(len(name) for name in names)
[len(name) for name in names]

max(names, key=lambda n:len(n))

# Define extremes below:
def extremes(nums):
    return min(nums), max(nums)