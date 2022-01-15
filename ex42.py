# 42 - Class

## Replace ?? with is-a or has-a

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):   #init needs self
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):   #init needs self
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):   #init needs self
        ## Person has-a name
        self.name = name
        ## Person has-a pet
        self.pet = None     # Default is None

## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):   #init needs self
        ## ?? hmm what is this strange magic?
        ## Runs the __init__ method of a parent class
        ## Employee has-a name
        super(Employee, self).__init__(name)    #init needs self
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")
## satan is-a Cat
satan = Cat("Satan")
## Mary is-a Person
mary = Person("Mary")

## ??
mary.pet = satan
## ??
frank = Employee("Frank", 120000)
## ??
frank.pet = rover

## ??
flipper = Fish()
## ??
crouse = Salmon()
## ??
harry = Halibut()