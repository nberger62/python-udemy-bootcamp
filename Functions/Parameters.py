
def square(num):
    return num * num
print(square(4))
print(square(8))


#Naming Parameters
#Not great!!!!!!!!!!!!!
def print_full_name(string1, string2):
    return(f"Your full name is {string1} {string2}")


# Better way of writing the function
def print_full_name(first_name, last_name):
    return(f"Your full name is {first_name} {last_name}")