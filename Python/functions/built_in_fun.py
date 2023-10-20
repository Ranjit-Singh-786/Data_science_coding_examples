# MAP , FILTER , REDUCE Functions example

# <<<<<<<<<<<<<<  EXAMPLES ON MAP() >>>>>>>>>>>>>>>>>>>>>>>>>>
# 1. EXAMPLE

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Define a function that squares a number
def square(x):
    return x ** 2

# Use map() to apply the function to each element in the list
squared_numbers = map(square, numbers)

# The result is an iterator, so convert it to a list to see the output
squared_numbers_list = list(squared_numbers)
print("using user defined function ",squared_numbers_list)


# 2. EXAMPLE using Lambda function

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

map_iterator = map(lambda x:x**2,numbers)
output_using_lambda = list(map_iterator)
print('output using lambda ',output_using_lambda)


# 3. EXAMPLE DEFINING OWN MAP FUNCTION
numbers = [1, 2, 3, 4, 5]

def fun(x):
    return x**2

def apna_map(fun,lst):
    temp = [] 
    for  item in lst:
        temp.append(fun(item))
    return temp

apna_output = apna_map(fun,numbers)
print("output from apna map function :- ",apna_output)



# <<<<<<<<<<<<<<  EXAMPLES ON FILTER() >>>>>>>>>>>>>>>>>>>>>>>>>>
# 1. EXAMPLE ON EVEN NUMBER USING USER DEFINED FUNCTION

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define a function to check if a number is even
def is_even(x):
    return x % 2 == 0

# Use filter() to get a list of even numbers
even_numbers = list(filter(is_even, numbers))

print("even number filtered using filter function :-",  even_numbers)



# 2. EXAMPLE ON EVEN NUMBER USING LABMDA FUNCTION

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_output_iterator = filter(lambda x: x%2==0,numbers)
even_numbers = list(filter_output_iterator)
print('even number using lambda function :-',even_numbers)