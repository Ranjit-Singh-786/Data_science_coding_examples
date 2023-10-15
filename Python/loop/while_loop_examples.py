# 1. write a program to print hello world 10 times

# i = 0
# while i <=10:
#     print('Hello world !')
#     # i +=1
#     i = i + 1

#2. Counting from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1


# 3. Calculating the sum of numbers. and number will be passed by the user.

number = int(input('enter your number :-'))
temp = 0
i = 0
while i <= number:
    temp +=i
    i+=1
print(f"sum of your number {number} is :- {temp}")


# 4. Printing even numbers from a user range.

user_range = int(input('Type your range in which, you want even numbers :- '))
i = 0
while i <=user_range:
    print(i,end="")
    i +=2

# # 3. number guessing program
# import random

# guess_number = int(input('Please guess your number :-'))
# target_number = random.randint(1,100)
# condition = True
# while condition:
#     if guess_number == target_number:
#         print(f'you are great, you guessed {guess_number}')
#     if guess_number <= target_number:
#         print(f"your is to low {guess_number}")
#         print('please select another number.','\n')
#         guess_number = int(input('please guess your number :-'))


