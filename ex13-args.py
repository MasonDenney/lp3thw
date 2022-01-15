# 13 - Params, Unpacking and Vars

# Must give 3 additional args to work
# Run using:
# python3 ex13-args.py 1 2 3

from sys import argv

script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
