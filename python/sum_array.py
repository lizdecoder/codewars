# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

# Examples

# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2

# Input: []
# Output: 0

# Input: [-2.398]
# Output: -2.398

# original attempt
# def sum_array(a):
#     return sum(num for num in a)

# refractored
def sum_array(a):
    return sum(a)
    

s = sum_array([1, 5.2, 4, 0, -1])
# s = sum_array([])
# s = sum_array([-2.398])
print(s)