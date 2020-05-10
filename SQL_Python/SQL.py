import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO friends
                        # VALUES ('Merriwether', 'Lewis', 7)'''

data = ("Nathan", "Berger", 25)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)
# commit changes
conn.commit()
conn.close()


