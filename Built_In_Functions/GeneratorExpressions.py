#not sure why we went over this lol, won't use much
# only use the gen function if you are doing it once
#def gen():
 #   return (something for something in get_some_stuff())
#print(gen()[:2]) #don't support indexing or slicing
#print [5,6] + gen() # generators can't be added to lists


#Traceback (most recent call last):
  #File "C:/Users/Nathan Berger/PycharmProjects/Built_In_Functions/GeneratorExpressions.py", line 5, in <module>
   # print(gen()[:2]) #don't support indexing or slicing
 # File "C:/Users/Nathan Berger/PycharmProjects/Built_In_Functions/GeneratorExpressions.py", line 4, in gen
   # return (something for something in get_some_stuff())
#NameError: name 'get_some_stuff' is not defined

#
import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")

#To do the same thing, it takes...
#List Comprehension: 9016 bytes
#Generator Expression: 112 bytes