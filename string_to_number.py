# We need a function that can transform a string into a number. What ways of achieving this do you know?

# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

# str = "1234"
# str = "605"
str = "1405"

def toNumber(str):
	return int(str)

number = toNumber(str)
print(number)
print(type(number))