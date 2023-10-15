# <<<< 1st example on conditional statement to check the user input url is valid or not
# <<<< if url is valid then find the Ip adrees throught the DNS.

import requests
import socket
from urllib.parse import urlparse

# to get the user input url
user_input_url = input('Please Enter Your url :- ')

# requesting user input url
response = requests.get(user_input_url)

if response.status_code < 400:    # if it is true then URL is valid
    print(f"This is valid URL we got response from the server side.")

    # fetching base url through the Api to get Ip Adress
    base_url = urlparse(user_input_url).netloc

    # fetching base url through string slicing to get Ip Adress
    
    # fetching_base_url = user_input_url[8:]
    # base_url = fetching_base_url[ : fetching_base_url.find('/')]


    # fetching the Ip Adress through the DNS 
    ip = socket.gethostbyname(base_url)

    if ip:
        print(f'User input Url :- {user_input_url}','\n')
        print(f"Base url :- {base_url}",'\n')
        print(f"DNS name :- {base_url} and Ip adress is :- {ip}")

    else:
        print(f"sorry we did,nt get ip address")
else:
    print(f"This is your invalid url :- {user_input_url}")





### <<<<< 2nd. Example on find the largest number in between 3 user input.  >>>>>>

num1 = int(input('enter your first number :- '))
num2 = int(input('enter your  second number :-'))
num3 = int(input('enter your third number :- '))
print('\n')


if num1 >= num2 and num1 >= num3:
    print(f"num1 is a largest number :- {num1}")

elif num2 >= num1 and num2 >= num3:
    print(f"num2 is a largest number :- {num2}")

else:
    print(f"num3 is a largest number :- {num3}")




### <<<< 3rd Example on find the prime from userinput with nested if else to find the range of user input. >>>>>


num = int(input('enter your  number :- '))
if num >0:
    if num %2==0:
        print(f"number is prime :- {num}")

            #nested if - else to find  the range of
        if (num >= 0) & (num <= 50):
            print('this number is in between 0 - 50 range.')
        
        else:
            print('number is largest  than 50.')


    else:
        print(f"number is odd :- {num}")
            #nested if - else to find  the range of
        if (num >= 0) & (num <= 50):
            print('this number is in between 0 - 50 range.')
        

        else:
            print('number is largest  than 50.')
else:
    print('please enter a number greater than 0 ')