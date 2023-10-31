class Student:
    hello = "Hello from class"
    def __init__(self,roll_no,name,branch,college,hello):
        # constructor
        self.roll_no = roll_no     # intance variable
        self.name = name
        self.branch = branch
        self.college = college
        self.hello = hello

    #instance method
    def student_record(self):
        print("Class Variable :-",Student.hello)
        print()
        print(self.hello)
        print(self.roll_no)
        print(self.name)
        print(self.branch)
        print(self.college)


        
#object creating
obj = Student(1,"Ranjit Singh",'CSE','IET Agra','Hello from instance')

#calling instance method
obj.student_record()