# 1. Single Inheritence using constructor

class Parent:
    def __init__(self,father_name , mother_name , address):
        self.father_name = father_name
        self.mother_name = mother_name
        self.address = address

    def intro(self):
        print(f"my father name is :- {self.father_name}")
        print(f"my mother name is :- {self.mother_name}")
        print(f"and i am from {self.address}")

class child(Parent):
    def __init__(self,my_name,my_profesion,my_company,father_name,mother_name,address):
        self.my_name = my_name
        self.my_profesion = my_profesion
        self.my_company = my_company
        super().__init__(father_name=father_name,mother_name=mother_name,address=address)

    def full_intro(self):
        self.intro()       # calling parent class function inside the child class function.
        print(f"my name is {self.my_name}")
        print(f"i am working as {self.my_profesion}")
        print(f"and i am working in {self.my_company}")


    def access_instance_var(self):
        """now i am trying to get instance variable from parent class"""
        my_intro = f"""my name is {self.my_name} , and i am from {self.address}
        i am workin in {self.my_company} as a {self.my_profesion}"""
        print(my_intro)




child_class_obj = child(my_name='Ranjit Singh',my_profesion='Data Scientist',my_company='google',father_name='somveer singh',mother_name='akhalesh devi',address='mathura uttar pradesh')


child_class_obj.intro()  # <<---- calling parent class method
print()
child_class_obj.full_intro()
print()
child_class_obj.access_instance_var()
