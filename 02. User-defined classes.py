# user-defined classes in python, may be created using the class keyword with any name you want.

# ============================================================================================
# Create a class and "self" keyword in python
# ============================================================================================

class Person:
    def speak(self):
        print("hi hi..")


person1 = Person()  # create an object/instance of the Dog class
person1.speak()

# in the above class, "self" keyword refers to the instance of the class. in Python, "self" keyword is used inside a class that refer to the instance of the class.
# "self" allows the method to access the instance of the class. "self" is the first parameter of any method in a class in python.

# ============================================================================================
# __init__() method in python
# ============================================================================================


class Person1:
    def __init__(self, name, age):  # catch the values passed to the class from the object
        self.name = name
        self.age = age

    def speak(self):
        print("hi hi..")


person2 = Person1("John", 23)  # passing the values to the __init__() method
print(person2.name)
print(person2.age)
person2.speak()

# in the above class, __init__() method is a special method in Python classes. It is called a constructor in object-oriented terminology.
# it will be called when an object is created. The __init__() method is called automatically when an object is created.
# It is used to initialize attributes for the object.

# ============================================================================================
# Relationship between class and object in python
# =================================================================================

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Owner:
    def __init__(self, name, address, contactNumber):
        self.name = name
        self.address = address
        self.phoneNumber = contactNumber 
        

owner1 = Owner("John", "123, Colombo, Sri Lanka", "077123456711")
dog1 = Dog("Tommy", "German Shepherd", owner1)
print(dog1.owner.name)

owner2 = Owner("Smith", "456, Colombo, Sri Lanka", "077123456722")
dog2 = Dog("Jimmy", "Golden Retriever", owner2)
print(dog2.owner.name)
