#15 - Read Files

# Needs filename as arg
# Run using python3 ex15-readfiles.py ex15-input.txt

from sys import argv
script, filename = argv

# Using arg
txt = open(filename)
print(f"Here's your file {filename}:")
print(txt.read())

# Using input
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())