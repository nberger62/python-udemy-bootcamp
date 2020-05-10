from csv import reader
with open("fighters") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        print(row)

# ['Name', 'Country', 'Height']
# ['bill', 'Japan', '6']
# ['nathan', 'US', '7']
# ['sally', 'china', '4']
# ['tom', 'sweden', '5']

