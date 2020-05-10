#makes a new zip list formed together, like a zip file
#list tuples

first_zip = zip([1,2,3,4], [4,5,6,7])
list(first_zip)
dict(first_zip)

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

# final_grades = {'dan': 98, 'ang': 91, 'kate': 78}

# final_grades = [max(pair) for pair in zip(midterms, finals)]

final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}

print(final_grades)

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

# final_grades = {'dan': 98, 'ang': 91, 'kate': 78}

# final_grades = [max(pair) for pair in zip(midterms, finals)]

# final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}
final_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)

print(final_grades)

def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))


def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))