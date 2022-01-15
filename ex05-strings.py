#5 - More Variables and Printing
# var names must begin with a char not a num
# Strings can use single or double quotes
my_name = "Zed A. Shaw"
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# Without f prefix it actually prints the curly braces and var name 
print("Let's talk about {my_name}.")

# format-strings(f-strings) are special strings that begin with f
# used to format a String with other variables
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")