# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0  # no characters repeats more than once
# "aabbcde" -> 2  # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1  # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2  # 'a' and '1'
# "ABBA" -> 2  # 'A' and 'B' each occur twice

# original attempt
# def duplicate_count(text):
#     duplicate = []
#     print(set(text))
#     for char in text.lower():
#         if(not(char in duplicate) and text.lower().count(char) > 1):
#             duplicate.append(char)
#     return len(duplicate)

# clever attempt
def duplicate_count(text):
    # set() removes duplicates
    return len([c for c in set(text.lower()) if text.lower().count(c) > 1])

# duplicates = duplicate_count("abcde")
duplicates = duplicate_count("aabbcde")
# duplicates = duplicate_count("aabBcde")
# duplicates = duplicate_count("indivisibility")
# duplicates = duplicate_count("Indivisibilities")
# duplicates = duplicate_count("aA11")
# duplicates = duplicate_count("ABBA")
print(duplicates)
