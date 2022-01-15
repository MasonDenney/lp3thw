#38 - Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
"Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #pop take last in list
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)
# There we go:  ['Apples', 'Oranges', 'Crows', # 'Telephone',
#  'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']

print("Let's do some things with stuff.")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())      #Corn is last in list

#A string can use .join() to insert itself between items in a list
print(' '.join(stuff))
print('#'.join(stuff[3:5])) #fourth and fifth items only

