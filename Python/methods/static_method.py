class Student:

    # class variable
    hello = "Hello from class"
    name = 'Radhey'
    branch = 'IT'
    college = "IET Lucknow"

    # constructor
    def __init__(self,roll_no,name,branch,college,hello):
        self.roll_no = roll_no     # intance variable
        self.name = name
        self.branch = branch
        self.college = college
        self.hello = hello

    #class method
    @classmethod
    def class_student_record(cls):
        print("Class Variable :-",cls.hello)
        print()
        print(cls.name)
        print(cls.branch)
        print(Student.college)  # you can also access using class name instead of cls keyword

        # print()
        # print(self.hello)


        #instance method
    def student_record(self):
        print("Class Variable :-",Student.hello)
        print()
        print(self.hello)
        print(self.roll_no)
        print(self.name)
        print(self.branch)
        print(self.college)

# Defining Static method
    @staticmethod
    def static_method():
        name = "ROCKY 😎"
        branch = "KGF"
        roll_no = 1
        college = "Mummai"

    #accessing static property
        print('accessing static property')
        print(name)
        print(branch)
        print(roll_no)
        print(college)
        print()
    # accessing class property
        print('accessing class property using static method')
        print(Student.name)                
        print(Student.branch)                
        print(Student.college)                




#object creating
obj = Student(1,"Ranjit Singh",'CSE','IET Agra','Hello from instance')


# calling class method
print('output from class method ')
Student.class_student_record()
obj.class_student_record()   # you can call using object or class name

print()



#calling instance method
print('output from instance method')
obj.student_record()


print('output from static method')
obj.static_method()