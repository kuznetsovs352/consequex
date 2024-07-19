fileName = "example.txt"

# You can use fileName in various ways, for example:
with open(fileName, 'r') as file:
    content = file.read()
    # Process the content or perform other file operations

# Or check the file extension:
if fileName.endswith(".txt"):
    # Do something specific for .txt files
