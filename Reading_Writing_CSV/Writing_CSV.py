from csv import writer
with open("cats.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerrow(["Name", "Age"])
    csv_writer.writerrow(["Blue", 3])
    csv_writer.writerrow(["Kitty", 1])
