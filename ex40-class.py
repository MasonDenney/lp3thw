#40 - Modules, Classes and Objects

# When import module, only one instances
# Classes are blueprints used to make many instances

################################################################
#MODULE
'''
#Module in mystuff.py
def apple():
        print("apple")
bb = "xx"

#main.py
import mystuff
mystuff.apple()
print(mystuff.bb)
'''
#CLASS
'''
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)
'''
################################################################

#Class
class Song(object):

    def __init__(self, lyrics):     #init needs self
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Create two Song objects using class
happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])

# Test
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()