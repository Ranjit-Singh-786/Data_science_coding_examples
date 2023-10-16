# 1. Create a function that takes two numbers as input and returns their sum.

# function defining
def add_numbers(a, b):
    return a + b  

# calling function
result = add_numbers(3, 5)
print(result) 

# 2. Write a function that takes a list of numbers as input and returns the sum of all the even numbers in the list.
def sum_even_numbers(lst):
    sum_even = 0
    for num in lst:
        if num % 2 == 0:
            sum_even += num
    return sum_even

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(numbers)
print(result)


# 3. Create a function that takes a string as an input and returns a dictionary containing the count of each character in the string.
def count_characters(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = input_string.count(char)
    return char_count

input_str = "upflairs pvt ltd jaipur rajsthan"
result = count_characters(input_str)
print(result)

# 5. write a function to genrate a table of user input number
def generate_table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")

number = int(input('please enter a number to generate a table :-'))
generate_table(number)

# 4. write a program to sort the given list without using built-in function

lst = [7,4,8,5,1,4,5,50,6,821,517,4,5,2,3,6,9]
def sort_list(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] >lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst

sorted_list = sort_list(lst)
print(f"your sorted list :- {sorted_list}")