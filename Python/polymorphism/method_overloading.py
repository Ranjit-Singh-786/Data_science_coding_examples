# # compile-time or static polymorphism achieved by method overloading

# 1. Example on polymorphism
def add(x, y, z = 0): 
    return x + y+z
 

print(add(2, 3))
print(add(2, 3, 4))