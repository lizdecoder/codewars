
numbers = [4, 566, 2, 1, 9, 63, -134, 6]

def max_number(numbers):
	max_num = 0
	for number in numbers:
		if max_num < number:
			max_num = number
	return max_num


max_num = max_number(numbers)
print(f'the max number is: {max_num}')

def min_number(numbers):
	min_num = 0
	for number in numbers:
		if min_num > number:
			min_num = number
	return min_num

min_num = min_number(numbers)
print(f'the min number is: {min_num}')