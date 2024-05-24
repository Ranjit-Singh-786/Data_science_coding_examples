from abc import ABC,abstractmethod 

#abstract class
class Manager(ABC): 
    Manager_name = "suresh chandra"
    Manager_email = "suresh@gmail.com"
    Manager_password = "hello@123"

    @abstractmethod   
    def Manager_details(self):
        pass 

# manager_obj = Manager()  #<-- cant create 
class Employee(Manager): 
    def __init__(self):
        self.employee_name = "Pappu"
        self.employee_email = "pappu@gmail.com"

    def Manager_details(self):
        print("Manager name : ",self.Manager_name)
        print("Manager email : ",self.Manager_name)


    def employee_details(self):
        print("employee name : ",self.employee_name)
        print("employee email id : ",self.employee_email)


#initiating object of Employee 
emp_obj = Employee()

#calling Manager method
emp_obj.Manager_details()
print()

emp_obj.employee_details()
    

