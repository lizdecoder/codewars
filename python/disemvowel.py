# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

# orginial attempt
# def disemvowel (str):
#     for letter in str:
#         str.lower()
#         if letter == "o" or letter == "a" or letter == "u" or letter == "i" or letter == "e":
#             str = str.replace("o", "").replace("O", "")
#             str = str.replace("a", "").replace("A", "")
#             str = str.replace("u", "").replace("U", "")
#             str = str.replace("i", "").replace("I", "")
#             str = str.replace("e", "").replace("E", "")
#     return str

# refractored
# def disemvowel (str):
#     for char in str:
#         if char in "aeiou" or char in "aeiou".upper():
#             str = str.replace(char, "")
#     return str

def disemvowel (str):
    for char in str:
        if char in "aeiouAEIOU":
            str = str.replace(char, "")
    return str


v = disemvowel("This website is for losers LOL!")
print(v)