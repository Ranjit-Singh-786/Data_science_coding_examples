# 1. write a program to print hello world 10 times

# solution 1st
for i in range(0,10):
    print(f"{i} Hello world !")

# solution 2nd
for i in range(10):
    print(f"{i} Hello world !")


# 2.can we traverse each element from given string
organization_name = "Upflairs in jaipur Rajsthan"
for char in organization_name:
    print(char)



# 2.find a target element from the list

lst = [52,45,85,96,56,47,85,95,5,12,75,48,96,45,85,4,11,22,33,52]
target = 95

for index , item in enumerate(lst):
    if target == item:
        print(f"This is the index position of your target element :- {index}")
    else:
        print(f"Target element not found !")




# 3. find the character in a string using for loop

organization_name = "Upflairs in jaipur Rajsthan"
target = 'jai'
for index , char in enumerate(organization_name):
    if char == target:
        print(f"This is the index position of your target element :- {index}")
    else:
        print(f"Target element not found !")


# 4. write a program to count char in string using for loop
sentence = "india is a great country and i proud on myself that i am indian."

output_dict = {}
for char in sentence:
    output_dict[char] = sentence.count(char)
print(output_dict)



# 5.write a program to count char in string using for loop. and return only those char which are occured,
# more than 3 times

sentence = "india is a great country and i proud on myself that i am indian."

output_dict = {}
for char in sentence:
    output_dict[char] = sentence.count(char)

temp_list = []
for key , value in output_dict.items():
    if value >= 3:
        temp_list.append(key)
print(f"All are character which are occured more than 3 times :- {temp_list}")


# 6. Find the maximum element without using inbuilt fucntion from a given list.

item_list = [74,56,41,2,36,5,4,9,89,85,21,45,63,412,5,8,96,42,55,63]

temp = item_list[0]
for item in item_list:
    if temp < item:
        temp = item
print(f'this is your maximum element from the given list :- {temp}')


# 6. Find the minimum element without using inbuilt fucntion from a given list.

item_list = [74,56,41,2,36,5,4,9,89,85,21,45,63,412,5,8,96,42,55,63]

temp = item_list[0]
for item in item_list:
    if temp > item:
        temp = item
print(f'this is your minimum element from the given list :- {temp}')


