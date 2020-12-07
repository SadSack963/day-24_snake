
# We must remember to close the file with this method
# file = open("high_score.txt", mode="at")
# file.write("Hello World!\n")
# file.close()

# file = open("high_score.txt", mode="rt")
# contents = file.read()
# print(contents)
# file.close()

# Using "with", the file is closed automatically
with open("high_score.txt", mode="at") as file:
    file.write("Hello World!\n")

with open("high_score.txt", mode="rt") as file:
    contents = file.read()
    print(contents)
