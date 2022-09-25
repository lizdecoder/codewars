# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

# Examples:

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"

s = 'test'
# s = 'testing'
# s = 'middle'
# s = 'A'

# original attempt
# def get_middle(s):
# 	mod = len(s) % 2
# 	if mod != 0:
# 		index1 = len(s)/2
# 		return s[int(index1)]
# 	elif mod == 0:
# 		index1 = len(s)/2
# 		index2 = index1 - 1
# 		return s[int(index2)]+s[int(index1)]

# refractored
def get_middle(s):
	mod = int(len(s)/2)
	return s[mod] if len(s)%2!=0 else s[mod-1:mod+1]

# clever solution
def get_middle(s):
	# '//' floor division: divides & returns the int value of the quotient
	# and removes the digits after the decimal
	return s[(len(s)-1)//2:(len(s)+2)//2]


print(get_middle(s))