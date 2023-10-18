# 1. List comprehension example

temp = []
for i in range(1,11):
    temp.append(i)
print(temp)

# using list comprehension
temp = [i for i in range(1,11)]
print(temp)




# 2. Example on square

temp = []
for i in range(1,11):
    temp.append(i**2)
print (temp)

# Using list comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)


# 3. Example on even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list()
for i in numbers:
    if i%2==0:
        even_list.append(i)

# Using List comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)


# 4. example on even and odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp = [] 
for i in numbers:
    if i % 2 == 0:
        temp.append(i)
    else:
        temp.append('odd')
print(temp)


# using List comprehension with if-else
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [x if x % 2 == 0 else "odd" for x in numbers]
print(new_list)