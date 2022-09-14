# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

str = "017645238"

# my original solution
# def fakeBinary(str):
# 	new_str = ""
# 	for digit in str:
# 		if int(digit) < 5:
# 			digit = "0"
# 			new_str += digit
# 		else:
# 			digit = "1"
# 			new_str += digit
# 	return new_str

# updated solution
def fakeBinary(str):
	return "".join('0' if digit < '5' else '1' for digit in str)

updated_str = fakeBinary(str)
print(updated_str)