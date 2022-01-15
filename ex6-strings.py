#6 - Strings and Text
# Can put variables into strings using f-strings
types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# Below print will actually print the curly braces
print(joke_evaluation)
# Use .format() to format an existing string
print(joke_evaluation.format(hilarious))

# Add 2 strings together
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)