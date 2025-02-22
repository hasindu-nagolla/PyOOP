# Access Modifiers are used to restrict the access for the variables and methods in a class. Help to protect the data from accidental changes.

# => Public: eg: studentName, school, grade
# => Protected: eg: _studentName, _school, _grade
# => Private: eg: __studentName, __school, __grade


# ==================================================================
# 01. Make data as private and use getters and setters
# ==================================================================

# Traditional Getter Method

class Student:
    def __init__(self, studentName, school, email):
        self.studentName = studentName
        self.school = school
        self._email = email

    def getEmail(self):
        return self._email.lower()

    def setEmail(self, newEmail):
        self._email = newEmail.lower()


student1 = Student("Hasindu", "St' Thomas College", "Hasindu@gmail.com")
print(student1.getEmail())

student2 = Student("Lakshan", "Gov Science College", "Lakshan@gmail.com")
print(student2.getEmail())

student1.setEmail("abc@email.com")
print("Modified email is: ", student1.getEmail())
