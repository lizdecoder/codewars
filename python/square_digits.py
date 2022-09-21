# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

from turtle import numinput


digits = 9119

# my original attempt
# def square_digits(digits):
# 	digits = str(digits)	
# 	new_digit = ""
# 	for digit in digits:
# 		str_product = str(int(digit)*int(digit))
# 		new_digit += str_product 
# 	return int(new_digit)

# refractored
# def square_digits(digits):
# 	digits = str(digits)	
# 	new_digit = ""
# 	for digit in digits:
# 		new_digit += str(int(digit)**2)
# 	return int(new_digit)

# clever attempt
def square_digits(digits):
	return int(''.join(str(int(d)**2) for d in str(digits)))

ex = square_digits(digits)
print(ex)
print(type(ex))