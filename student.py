from user import User

class Student(User):
    pass

newUser = Student("tomashi","samyahoo.com","123456")

print(newUser.getUsername())  

newUser.setUsername("sam")