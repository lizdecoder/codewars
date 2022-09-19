# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# str = "jacoby" #2
# str = "gemuse" #3
str = "understanding" #4

# my original solution
# def vowel_count(str):
# 	count = 0
# 	for letter in str:
# 		if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
# 			print(letter)
# 			count += 1
# 	return count

# creative solution #1
# def vowel_count(str):
# 	return sum(1 for let in str if let in 'aeiou')

# creative soltion #2
def vowel_count(str):
	return sum(c in 'aeiou' for c in str)

counter = vowel_count(str)
print(counter)