# 44 - Inheritance

# Avoid Multiple Inheritence at all cost!

#a - Implicit Inheritance = child uses parent's function without its own
#b - Override
#c - Altered with Pre and Post
#d - All
class Parent(object):
    def override(self):
        print("PARENT override()")
    def implicit(self):
        print("PARENT implicit()")
    def altered(self):
        print("PARENT altered()")
class Child(Parent):
    #no implicit
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()  # parent imp
son.implicit()  # parent imp because not defined for child
dad.override()  # parent over
son.override()  # child over
dad.altered()   # parent alt
son.altered()   # child pre, parent alt, child post


# super() most commonly used in __init__ fuctions in base class
#class Child (Parent):
#    def __init__(self, stuff) :
#        self.stuff = stuff
#        super(Child, self).__init__()

###################################################################
# Composition instead of Inheritance

# Use composition to package code into modules that can be used
# in many unrelated and different places/situations

class Other(object):
    def override(self):
        print("OTHER override()")
    def implicit(self):
        print("OTHER implicit()")
    def altered(self):
        print("OTHER altered()")

class Child(object):
    def __init__(self):
        self.other = Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()
son.implicit()  #other imp
son.override()  #child over
son.altered()   #child pre, other alt, child post

# To Study, check PEP 8 Style Guide at
# https://www.python.org/dev/peps/pep-0008/