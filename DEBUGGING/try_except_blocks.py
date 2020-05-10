# use try and except block

#foobar example
#try:
    #foobar
#except: # you really should state which error on this line to be specific, such as NameError
    #print("problem")
#print("after the try")



def get(d,key):
    try:
       return d[key]
    except KeyError:
        return None
d = {"name": "Ricky"}
print(get(d, "city"))


try:
   num = int(input("please enter a number: "))
except:
    print("Not a number")


def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("soemthin went wrong")
    except TypeError as err:
        print("a or b must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")
#print(divide(1,2))
print(divide(1,'a'))
