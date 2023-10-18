# 1. Break keyword in loop, it is used for to break the execution of the loop.

for i in range(1,11):
    print(i)
    if i == 6:
        break

print()

# 2. continue keyword to ignore the specific iteration of the loop

for i in range(1,11):
    if i == 6:
        continue
    print(i)


# 3.example on break keyword 
while True:
    inpt = input('Do you want to quiet it Y/N :-')
    if inpt == "y":
        break
    else:
        print("This is your input :-",inpt)

# 4. example on break keyword
sentence = input('please enter your sentence :-')
for char in sentence:
    if  char =="y":
        break
    else:
        print(char)

# 5. example

i = 0
while i < len(sentence):
    if sentence[i] == 'y':
        break
    else:
        print(sentence[i])
    i+=1

# 6. example

sentence = input('please enter your sentence :-')
while True:
    for i in range(len(sentence)):
        if sentence[i] == 'y':
            break
        else:
            print(sentence[i])
    break
