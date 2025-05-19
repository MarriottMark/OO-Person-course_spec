class Person:
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
    
    def PrintFullName(self):
        print(self.FirstName + " " + self.LastName)

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
    def __init__(self, Occupation):
        self.Occupation = Occupation
        self.Alumni = False
    
    def ShowOccupation(self):
        print(self.Occupation)


    def SetAlumni(self, Alumni):
        self.Alumni = Alumni
       
    def DisplayAlumni(self):
        if self.Alumni == True:
            print("This parent is an alumni")
        else:
            print("This parent is not an alumni")


class Subject():
    def __init__(self):
            return

    

class Teacher():
    def __init__(self, Title, LastName):
        self.LastName = LastName
        self.Title = Title
        self.Subject = []
    

    def ShowClasses(self):
        for sub in self.Subject:
            print(sub)
    
    def EnrollClass(self, SubjectName):
        self.Subject.append(SubjectName)
    
    def ShowName(self):
        print(self.Title + " " + self.LastName)



# Main program
print("Student: \n")
s1 = Student("Troy", "Harcoan", "6", "Heber")
s1.EnrollClass("Maths Advanced")
s1.EnrollClass("English Advanced")
s1.EnrollClass("Ancient History")
s1.EnrollClass("Music")  
s1.EnrollClass("Software Engineering")
s1.EnrollClass("Biology")
s1.ShowClasses()
s1.PrintFullName()
print("Dad: \n")
p1 = Parent("Makes lights")
p1.SetAlumni(True)
p1.ShowOccupation()
p1.DisplayAlumni()
print("Teacher: \n")
t1 = Teacher("Mr.", "Smith")
t1.EnrollClass("Maths Advanced")
t1.ShowClasses()
t1.ShowName()
