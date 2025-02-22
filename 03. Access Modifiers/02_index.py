# ======================================================================
# Property Method (Encapsulation + Abstraction), Getter and Setter
# ======================================================================

class Student:
    
    def __init__(self, studentName, school, email):
        self.studentName = studentName
        self.school = school
        self._email = email
    
    # Getter property
    @property
    def email(self):
        print("Getting email")
        return self._email
    
    # Setter property
    @email.setter
    def email(self, newEmail):
        if '@' in newEmail:
            print("Setting email")
            self._email = newEmail
    
    
student1 = Student("Hasindu", "St' Thomas College", "hasindu@gmail.com")
print(student1.email)

student1.email = "abc@gmail.com"
print(student1.email)

