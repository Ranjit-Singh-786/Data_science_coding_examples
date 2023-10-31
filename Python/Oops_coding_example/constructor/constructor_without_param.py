class Bank:
    name = "Ranjit"    # class variable

    #without parameters
    def __init__(self):
        self.name = 'Ranjit Singh'
        self.account_number = 246101041407
        self.address = "Mathura UP"


    # instance method
    def show_info(self):
        print('showing the information of account holder ','\n')
        print(self.name)
        print(self.account_number)
        print(self.address)



#creating object of the class
account_1 = Bank()
account_1.show_info()
