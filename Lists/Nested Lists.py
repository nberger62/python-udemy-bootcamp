#nested lists can be used for game building like a maze, web development, data science

#nested lists have lists within lists

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0][1])
# 2

print(nested_list[-1][-2])
# 8

nested_list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for val in nested_list2:
        for val in 1:
            print(val)

#Quiz
answer = [[i for i in range(0,3)] for num in range(0,3)]

