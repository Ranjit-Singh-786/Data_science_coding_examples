# 1. write a program to print hello world 10 times

i = 0
while i <=10:
    print('Hello world !')
    # i +=1
    i = i + 1

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

# 5. Generate table using while loop
user_num = int(input('enter your number in which table you want to create :-'))
i = 1
while i <=10:
    print(f"{user_num} * {i} = {user_num * i}")
    i+=1

# 5. number guessing program
import random

guess_number = int(input('Please guess your number :-'))
target_number = random.randint(1,20)
wrong_guessed_numbers = []
attempt = 0
condition = True
while condition:
    if guess_number == target_number:
        print(f'you are great, you guessed This number {guess_number} in only {attempt} attempts.')
        print(f"you have wrognly guessed these numbers :- {wrong_guessed_numbers}")
        condition = False

    elif guess_number <= target_number:
        print(f"sorry you are too low {guess_number}")
        print('please select larger number than this.','\n')
        guess_number = int(input('please again guess your number :-'))
        wrong_guessed_numbers.append(guess_number)
        attempt += 1

    else:
        print(f"sorry you are too high {guess_number}")
        print('please select lower number than this.','\n')
        guess_number = int(input('please again guess your number :-'))
        wrong_guessed_numbers.append(guess_number)
        attempt += 1


    


