def write_file(file_name, file_content):
    """Writes file_content to file_name.txt, overwriting if it exists."""
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)


def append_file(file_name, file_content):
    """Appends file_content to file_name.txt."""
    with open(f"{file_name}.txt", "a") as file:
        file.write(file_content)


def read_file(file_name):
    """Reads and returns the content of file_name.txt."""
    with open(f"{file_name}.txt", "r") as file:
        return file.read()

write_file("lib/test_file", "Hello World\n")
append_file("lib/test_file", "Appended content.\n")
content = read_file("lib/test_file")
print(content)
