
# 1. Example on ValuError
try:
    user_input = int(input('Please enter your input :- '))
    print(user_input)
except ValueError:
    print('you have inserted wrong information.')


# ALSO CAN WRITE SAME CODE IN THIS WAY

try:
    user_input = int(input('Please enter your input :- '))
    print(user_input)
except ValueError as v:
    print('you have inserted wrong information.','\n')
    print(v)
except TypeError as tp:
    print('please make data type similar')
    print(tp)
except SyntaxError as se:
    print('please fix your sytnex')
except Exception as e:
    print(e)


# Example on 