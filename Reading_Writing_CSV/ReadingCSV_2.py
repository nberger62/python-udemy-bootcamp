from csv import reader
with open("fighters") as file:
    csv_reader = reader(file)
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")

# Name is from Country
# bill is from Japan
# nathan is from US
# sally is from china
# tom is from sweden

