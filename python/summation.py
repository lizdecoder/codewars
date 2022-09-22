# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

# For example:
# summation(2) -> 3
# 1 + 2
# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

# my original attempt
# def summation(num):
# 	num += 1
# 	sum = 0
# 	range_of_nums = range(num)
# 	for n in range_of_nums:
# 		sum += n
# 	return sum
	
# clever attempt
def summation(num):
	return sum(range(num+1))

sum_of_nums = summation(2)
print(sum_of_nums)