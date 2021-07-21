class Parent:
 def __init__(self,Fname,Iname):
    self.Fname = Fname
    self.Iname = Iname
 def printName(self):
    print(self.Fname,self.Iname)
class student(Parent):
    pass
newStudent = student("Sam", "Tomashi")
newStudent .printName()
