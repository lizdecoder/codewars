# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

# Examples(Operator, value1, value2) --> output
# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7

# my original attempt
# def basic_op(operator, value1, value2):
# 	if operator == '+':
# 		return value1+value2
# 	elif operator == '-':
# 		return value1-value2
# 	elif operator == '*':
# 		return value1*value2
# 	else:
# 		return value1/value2

# clever solution
def basic_op(operator, value1, value2):
	return eval(f'{value1}{operator}{value2}')

sum = basic_op('+', 4, 7)
sub = basic_op('-', 15, 18)
multi = basic_op('*', 5, 5)
division = basic_op('/', 49, 7)
print(sum, sub, multi, division)