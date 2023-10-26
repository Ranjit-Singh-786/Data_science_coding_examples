# i am defining custome error class
class CustomError(Exception):
    def __init__(self,custome_error_message):
        self.custome_error_message = custome_error_message
        super().__init__(custome_error_message)


# Defining a function not a method
def divide(x,y):
    if y==0:
        raise CustomError('bade bhaiya zero he🤣😂')
    else:
        return x / y


# now calling the function
try:
    result = divide(10,0)
    print("result of your divide :-",result)

except CustomError as e:
    print(e)

else:
    print('successfully divided !')

finally:
    print('imported taks also has been done !')


