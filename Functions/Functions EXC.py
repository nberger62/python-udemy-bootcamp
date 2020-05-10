'''
product(2,2) # 4
product(2,-2) # -4
'''

# define product below:
def product(num1, num2):
    return num1*num2
print(product(2,2))


'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if num > 0 and num <= len(days):
               return days[num-1]
    return None

'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(1):
    if l:
        return l[-1]
    return None