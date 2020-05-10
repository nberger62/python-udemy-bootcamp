#filter : Returns filter objects which can be converted into other iterables
#The object contains only the values that return true to the lambda

#evens = list(filter(lambda x: x % 2 == , 1))
#evens # 2, 4

#using filters and maps
[user for user in users if not user["tweets"]]

usernames = list(map(lambda user: user["username"].upper(),
     filter(lambda u: not u['tweets'], users))

def remove_negatives(nums):
    return list(filter(lambda l: l >= 0, nums))