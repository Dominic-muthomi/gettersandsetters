class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def getUsername(self):
        return self.username

    def setUsername(self,username):
        self.username = username    

class Student(User):
    pass
newUser = Student("tomashi","samyahoo.com","123456")
print(newUser.getUsername())  

newUser.setUsername("sam")
print(newUser.getUsername()) 