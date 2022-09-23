# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

# Example:
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

# my original attempt
# def to_jaden_case(string):
# 	string = string.split(" ")
# 	new_list = []
# 	for word in string:
# 		word = word.capitalize()
# 		new_list.append(word)
# 	string = " ".join(new_list)
# 	return(string)

# clever attempt
def to_jaden_case(string):
	return ' '.join(word.capitalize() for word in string.split())

str = to_jaden_case("How can mirrors be real if our eyes aren't real")
print(str)

