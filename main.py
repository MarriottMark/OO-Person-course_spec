class Person:
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
    
    def PrintFullName(self):
        return

class Student(Person):
    def __init__(self, FirstName, LastName, StudentID, HouseGroup):
        super().__init__(FirstName, LastName)
        self.StudentID = StudentID
        self.HouseGroup = HouseGroup
        self.Subjects = []
    
    def EnrollClass(self, SubjectName):
        self.Subjects.append(SubjectName)
        
    def ShowClasses(self):
        for sub in self.Subjects:
            print(sub)


class Parent(Person):
    def __init__(self, Occupation, Alumni):
        self.Occupation = Occupation
        self.Alumni = Alumni
    
class Subject():
    def __init__(self):
        return
 
s1 = Student("Slirting", "Knox", "at least 3", "Broadton")
s1.EnrollClass("gup")
s1.ShowClasses()