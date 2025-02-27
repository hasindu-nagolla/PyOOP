# ==================================================================
# Static Attributes
# ==================================================================

# Static Attributes(Class Attributes) are shared among all instances of a class.
# They are defined at the class level
# Outside of the __init__ method
# Accessed using the className.<attributeName> or self.<attributeName> syntax

# ==================================================================
# Instance Attributes
# ==================================================================

# Instance attributes are attributes that are specific to an instance of a class.
# They are stored within each individual object.
# in the __init__ method


class User:

    userCount = 0  # This is a static attribute

    def __init__(self, name, email):
        self.name = name # This is an instance attribute
        self.email = email  # Increment the userCount by 1, when a new object is created.
        User.userCount += 1

    def displayUser(self):
        print("Name is: ", self.name, " & Email is: ", self.email)


user1 = User("Hasindu", "hasindu@gmail.com")
user2 = User("Lakshan", "lakshan@gmail.com")

# Accessing the static attribute in the User class
print("Total number of users: ", User.userCount)

# Accessing the static attribute in the User class using the object
print("Total number of users: ", user1.userCount) 