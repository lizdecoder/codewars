# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

# original attempt
# def remove_char(s):
# 	string = list(s)
# 	string.remove(string[0])
# 	string.pop()
# 	return ''.join(string)

# clever attempt
def remove_char(s):
	return s[1 : -1]

# str = remove_char('hello')
# str = remove_char('goodbye')
str = remove_char('understanding')
print(str)