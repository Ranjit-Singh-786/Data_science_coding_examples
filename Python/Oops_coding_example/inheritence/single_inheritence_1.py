# 1. Single Inheritence without using constructor

class Parent:
    father_name = "somveer singh"
    mother_name = "meena devi"
    address = "mathura uttar pradesh"

    def intro(self):
        print(f"my father name is :- {self.father_name}")
        print(f"my mother name is :- {self.mother_name}")
        print(f"and i am from {self.address}")

class child(Parent):
    my_name = "Raja"
    profession = "Data scientist"
    company = "Google"

    def full_intro(self):
        self.intro()       # calling parent class function inside the child class function.
        print(f"my name is {self.my_name}")
        print(f"i am working as {self.profession}")
        print(f"and i am working in {self.company}")


child_obj = child()
# child_obj.intro()   # <<--- calling parent class method by child object


child_obj.full_intro()  # <<--- calling child class function


