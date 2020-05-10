total = 0

def increment():
    global total
    total += 1
    return total

print(increment())
# UnboundLocalError: local variable 'total' referenced before assignment

#Total is a global scope, and this is why you are getting an error, will be covered later!

#Does work with the global scope!
