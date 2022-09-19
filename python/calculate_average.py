# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

lst = []

# my attempt
# def average(lst):
# 	total = 0
# 	if len(lst) == 0:
# 		average = 0
# 	else:
# 		for num in lst:
# 			total += num
# 			average = total/len(lst)
# 	return average

# clever solution
def find_average(array):
    return sum(array) / len(array) if array else 0

avg = find_average(lst)
print(avg)
