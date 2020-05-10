# Red Green Refactor
# write a test that fails, then one that works with minimal code


# TTD - testing is everything!

# Assertions

def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y

print(add_positive_numbers(1, 1))
add_positive_numbers(1, -1)

# if a python file is run with the -O flag, it will ignore all assertions. This is why you cannot count on these to run!

self.assertEqual
self.asserNotEqual
self.assertTrue
self.assertFalse