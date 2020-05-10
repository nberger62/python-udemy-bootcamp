# absolute value
abs(-5)
abs(5)
abs(3.4444)
abs(-3.4444)

# only works with numbers, integers and floats

# sum

# round
round(3.156)


def max_magnitude(nums):
    return max(abs(num) for num in nums)


def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)

def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)
