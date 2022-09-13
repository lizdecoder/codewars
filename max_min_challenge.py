
numbers = [4, 566, 2, 1, 9, 63, -134, 6]

# numbers = [-7]

# def max_number(numbers):
# 	max_num = 0
# 	for number in numbers:
# 		if max_num == 0:
# 			max_num = number
# 		if max_num < number:
# 			max_num = number
# 	return max_num

def maximum (numbers):
	return max(numbers)


max_num = maximum(numbers)
print(f'the max number is: {max_num}')

# def min_number(numbers):
# 	min_num = 0
# 	for number in numbers:
# 		if min_num == 0:
# 			min_num = number
# 			if min_num > number:
# 				min_num = number
# 	return min_num

def minimum (numbers):
	return min(numbers)

min_num = minimum(numbers)
print(f'the min number is: {min_num}')