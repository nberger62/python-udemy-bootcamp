# use the yield instead of return word at the end of the function.

# can yield or return multiple times!

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count +=1
counter = count_up_to(5)

next(counter)
