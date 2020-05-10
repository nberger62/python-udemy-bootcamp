file = open('story')
print(file.read())

# with Blocks
file = open("story")
file.read()
file.close()

with open("story") as file:
    data = file.read()

print(data)



with open("haiku", "w") as file:
    file.write("Line of words\n")
    file.write("Nathan is awesome!!\n")
    file.write("Line of words!")
