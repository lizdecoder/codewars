# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

# my attempt
# def high_and_low(str):
# 	split_str = str.split()
# 	lst_str = list(split_str)
# 	high = 0
# 	low = 0
# 	for number in lst_str:
# 		number = int(number)
# 		if high == 0 or high < number:
# 			high = number
# 		if low == 0 or low > number:
# 			low = number
# 	return f"{high} {low}"

# clever attempt
def high_and_low(numbers):
	numbers = [int(c) for c in numbers.split(' ')]
	return f"{max(numbers)} {min(numbers)}"
	
sum = high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4") #42 -9
# sum = high_and_low("1 2 3") #3 1
print(sum)
# print(type(sum))


