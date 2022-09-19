# Given an array of integers, return a new array with each value doubled.
# example: [1,2, 3] --> [2, 4, 6]

arr = [2, 4, 6]

# my original attempt
# def doubleArray(arr):
# 	new_arr = []
# 	for number in arr:
# 		number *=2
		# new_arr.append(number) 
		# could also be new_arr.append(number*2) and remove previous line
# 	return new_arr

# clever attempt
def doubleArray(arr):
	return [2 * number for number in arr]

new_array = doubleArray(arr)
print(new_array)
