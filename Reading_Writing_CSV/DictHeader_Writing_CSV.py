from csv import writer, DictWriter
with open("cats", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows({
        "Name": "Garfield",
        "Breed": "Orange Tabby",
        "Age": 10
    })
