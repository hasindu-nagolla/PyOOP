# ======================================================
# object-to-object interaction in python
# ======================================================

class Student:
    def __init__(self, studentName, school, grade):
        self.studentName = studentName
        self.school = school
        self.grade = grade
    
    def conversation(self, student): # student, Where are coming from?
        print(f"Send a message to {student.studentName}: Hi {student.studentName}, how are you? i am {self.studentName}")

student1 = Student("Hasindu", "St' Thomas College", "A/L")
student2 = Student("Lakshan", "Gov Science College", "O/L")
student3 = Student("Kasun", "Royal College", "Grade 10")


student1.conversation(student2) # Send a message to Lakshan: Hi Lakshan, how are you? i am Hasindu
student2.conversation(student3) # Send a message to Kasun: Hi Kasun, how are you? i am Lakshan

# ======================================================
# Access object data in python
# ======================================================

print(student1.studentName)
print(student1.school)
print(student1.grade)
print(student2.studentName)

# ======================================================
# Modify object data in python
# ======================================================

student1.studentName = "Sithara"
student2.school = "St' Thomas College"

print(student1.studentName)
print(student2.school)
