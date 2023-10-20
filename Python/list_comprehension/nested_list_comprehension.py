# 1. Example for creating 2D list using lit comprehension.

print([[i for i in range(3)] for i in range(5)])

# OUTPUT 
# [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]

# 2. Example on traversing a 2D list metrics
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
traversed = [[nested_list[row][item] for item in range(len(nested_list[row]))] for row in range(len(nested_list))]
print(traversed)

# 3. Example on traversing a 2D list metrics with condition if element is even return True else False
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
traversed = [[True if nested_list[row][item] %2 ==0 else False for item in range(len(nested_list[row]))] for row in range(len(nested_list))]
print(traversed)

# 4. Flatten the 2D list using list comprehension

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([item for sublist in nested_list for item in sublist])