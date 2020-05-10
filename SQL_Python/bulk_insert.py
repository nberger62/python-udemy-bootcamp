import sqlite3
conn = sqlite3.connect("my_friends.db")
c = conn.cursor()


people = [
    ("Bill", "Sally", 8),
    ("Dorthy", "Smalls", 20),
    ("Henry", "Bigs", 15),
    ("Patrick", "Tee", 18)]

average = 0
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    average += person[2]
print(average/len(people))

# c.fetchall() will get you a list of all results
