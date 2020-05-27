# Python Lambda Example

print ("Example 1")
# Example 1 
num = lambda: True
print(num())

print ("Example 2")
# Example 2
num = lambda x: x + 5
print(num(10))

print ("Example 3")
# Example 3
add = lambda x, y : x + y
print(add(10, 20))

print ("Example 4")
# Example 4
add = lambda x, y : x + y
print(add(10, 20))
 
print("\nResult from a Function")
def add_func(x, y):
    return x + y

print(add_func(10, 20))