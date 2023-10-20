# Examples on Exception handling

# num1 = int(input('enter your first number :-'))
# num2 = int(input('enter your second number :-'))
# print('program execution started !','\n')
# result = num1/num2
# print('program execution completed !','\n')
# print('This is your result of division ',result)



#using Exception Handling
num1 = int(input('enter your first number :-'))
num2 = int(input('enter your second number :-'))
try:
    
    print('program execution started !','\n')
    result = num1/num2
    print('program execution completed !','\n')
    print('This is your result of division ',result)

except Exception as e:
    print('we got an error !','\n')
    print(e)  # it will print class of exception

else:
    print('No exception in Try block !')

finally:
    print('This is important !')

print('Still program is working !')

    