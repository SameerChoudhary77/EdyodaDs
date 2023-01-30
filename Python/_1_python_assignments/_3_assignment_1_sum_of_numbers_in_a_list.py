# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)

# Expected Output : 20

# Explanation:

# Summation should like 8+2+3+0+7 = 20

# Method 1: using def function

def sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print("Sum:",sum((8,2,3,0,7)))


# Method 2: Using sum function

list1 = [8,2,3,0,7]
 
total = sum(list1)
 
print("Sum of all elements in given list: ", total)