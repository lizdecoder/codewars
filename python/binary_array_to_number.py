# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

# Examples:

# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
# However, the arrays can have varying lengths, not just limited to 4.

# original
# def binary_array_to_number(arr):
#     binary = ''.join(str(num) for num in arr)
#     num = int(binary, 2)
#     return num

# refactored
def binary_array_to_number(arr):
    return int(''.join((str(num) for num in arr)), 2)

# clever solutions
# def binary_array_to_number(arr):
#     return int(''.join(map(str, arr)), 2)

# result = binary_array_to_number([0,0,0,1]) #1
# result = binary_array_to_number([0,0,1,0]) #2
# result = binary_array_to_number([1,1,1,1]) #15
result = binary_array_to_number([0,1,1,0]) #6

print(result)