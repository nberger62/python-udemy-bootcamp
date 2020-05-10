with open("haiku", "a") as file:
    file.write("APPENDING LATER!!!!!\n")
    file.seek(4)


with open("haiku", "r+") as file:
    file.write("Added using r+")


def copy(file_name, new_file_name):
    with open(file_name) as file:
        text=file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text)


def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text=file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])


def statistics(file_name):
    with open(file_name) as file:
        lines=file.readlines()

    return {"lines": len(lines),
            "words": sum(len(line.split(" ")) for line in lines),
            "characters": sum(len(line) for line in lines)}