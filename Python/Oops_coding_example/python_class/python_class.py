#defining class name
class Bank:

    # defining class properties e.g variable
    name = 'Ranjit Singh'
    age = 22
    address = 'Mathura UP'
    bank_name = 'canara bank'
    account = 246101041407

    # Defining method in class
    def show_info(self):
        # accessing class properties in method
        # print(Bank.name)
        print(self.name)
        print(self.age)
        print(self.address)
        print(self.bank_name)
        print(self.account)

#creating object or instance of class
account_1 = Bank()
print('name of the account holder :- ',account_1.name,' and account number is :- ',account_1.account)
print()

account_1.name = "Ranjit sharma"
print('account holder name is changed :-',account_1.name,'\n')

account_1.show_info()
print()
print('Second accountant Details  ')

# creating second object
account_2 = Bank()
print(account_2.name)


#calling the class method
print('showing account 1 information')
account_1.show_info()
print()

print('showing account 2 information')
account_2.show_info()
print()

