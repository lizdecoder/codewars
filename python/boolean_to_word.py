# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

# original solution
# def bool_to_word(boolean):
# 	return "Yes" if boolean == True else "No";

# refractored
# def bool_to_word(boolean):
# 	return "Yes" if boolean else "No";

def bool_to_word(boolean):
	return ['No', 'Yes'][boolean]


# bool = bool_to_word(True)
bool = bool_to_word(False)
print(bool)
# print(type(bool))