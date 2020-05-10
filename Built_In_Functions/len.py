#More on len, more detail. len({})
#__len__()
#len('hi') is really 'hi'.__len__()
#So Object Oriented programming

class SpecialList:

    def _init_(self, data):
        self._data = data

    def _len_(self): #returning 50
        return self._data._len_len() // 2

l1 = SpecialList([1,40,30,100])
l2 = SpecialList([1,3,4,5])


print(len(l1))
print(len(l2))
