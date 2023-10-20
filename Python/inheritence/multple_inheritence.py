# 1. Single Inheritence without using constructor
class GrandFather:
    def __init__(self,grandpaa_name,grandpaa_age,grandpa_health):
        self.grandpaa_name = grandpaa_name
        self.grandpaa_age = grandpaa_age
        self.grandpa_health = grandpa_health


    def grandpaa_hii(self):
        print('Hello my son,God bless you')
        print(f"this is your grandpa {self.grandpaa_name}")
        print(f"and now i am {self.grandpaa_age} yead old !")
        print(f'and still i am {self.grandpa_health}')


class Father:
    def __init__(self,father_name , mother_name , address):
        self.father_name = father_name
        self.mother_name = mother_name
        self.address = address

    def father_hii(self):
        print(f'hii son this is your father {self.father_name}')
        print(f"my father name is :- {self.father_name}")
        print(f"my mother name is :- {self.mother_name}")
        print(f"and i am from {self.address}")

class child(GrandFather , Father):
    def __init__(self,my_name,my_profesion,my_company,father_name,mother_name,address,grandpaa_name,grandpaa_age,grandpa_health):
        self.my_name = my_name
        self.my_profesion = my_profesion
        self.my_company = my_company

        # calling parent class constructor using class name instead of SUPER()

        GrandFather.__init__(self,grandpaa_name=grandpaa_name, grandpaa_age=grandpaa_age, grandpa_health=grandpa_health)
        Father.__init__(self,father_name=father_name,mother_name=mother_name,address=address)

    def full_intro(self):
        self.grandpaa_hii()       # calling grand father class function
        print()
        self.father_hii()       # calling Father class function inside the child class function.
        print()

        print(f"my name is {self.my_name}")
        print(f"i am working as {self.my_profesion}")
        print(f"and i am working in {self.my_company}")


    def access_instance_var(self):
        """now i am trying to get instance variable from parent class"""
        my_intro = f"""my name is {self.my_name} , and i am from {self.address}
        i am workin in {self.my_company} as a {self.my_profesion}"""
        print(my_intro)


child_class_obj = child(my_name='Ranjit Singh',my_profesion='Data Scientist',my_company='google',father_name='somveer singh',mother_name='akhalesh devi',address='mathura uttar pradesh',grandpaa_name='Ram singh',grandpaa_age=78,grandpa_health='perfect')


child_class_obj.grandpaa_hii()
print('<<<<<<<<<<<<<   >>>>>>>>>>>>>>>>>>>>')
print()
child_class_obj.father_hii()
print('<<<<<<<<<<<<<   >>>>>>>>>>>>>>>>>>>>')
print()
child_class_obj.full_intro()
