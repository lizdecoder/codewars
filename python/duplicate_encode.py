# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples

# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

# original attempt
# def duplicate_encode(word):
#     str = ""
#     word = word.lower()
#     for char in word:
#         count = word.count(char)
#         print(f"char: {char} count: {count}")
#         if count > 1:
#             str += ")"
#         else:
#             str += "("
#     return str

# clever attempt
def duplicate_encode(word):
    word = word.lower()
    return ''.join('(' if word.count(char) == 1 else ')' for char in word)


# enc = duplicate_encode("din")
# enc = duplicate_encode("recede")
enc = duplicate_encode("Success")
# enc = duplicate_encode("(( @")
# enc = duplicate_encode("( ( )") #)))))(

print(enc)
