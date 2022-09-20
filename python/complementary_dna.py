# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

# Example: (input --> output)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

dna = 'ATTGC'
# dna = 'GTAT'

# my first attempt
# def comp_DNA(str):
# 	new_str = ""
# 	for letter in str:
# 		if letter == 'A':
# 			letter = 'T'
# 			new_str += letter
# 		elif letter == 'T':
# 			letter = 'A'
# 			new_str += letter
# 		elif letter == 'G':
# 			letter = 'C'
# 			new_str += letter
# 		elif letter == 'C':
# 			letter = 'G'
# 			new_str += letter
# 	return new_str

# my second attempt using match-case
# def comp_DNA(str):
# 	new_str = ''
# 	for letter in str:
# 		match letter:
# 			case 'A': letter = 'T'
# 			case 'T': letter = 'A'
# 			case 'G': letter = 'C'
# 			case _: letter = 'G'
# 		new_str += letter
# 	return new_str

# clever solution
def DNA_strand(dna):
	return dna.translate(dna.maketrans('ATCG', 'TAGC'))

new_dna = DNA_strand(dna)
print(new_dna)
# print(type(dna))