# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

# original
# def likes(names):
#     names_length = len(names)
#     if names_length == 0:
#         return "no one likes this"
#     elif names_length == 1:
#         return f'{names} likes this'
#     elif names_length == 2:
#         return f'{names[0]} and {names[1]} like this'
#     elif names_length == 3:
#         return f'{names[0]}, {names[1]} and {names[2]} like this'
#     else:
#         count = names_length - 2
#         return f'{names[0]}, {names[1]} and {count} others like this'

# refractored
# def likes(names):
#     names_length = len(names)
#     count = names_length - 2
#     match names_length:
#         case 0:
#             return "no one likes this"
#         case 1:
#             return f'{names[0]} likes this'
#         case 2:
#             return f'{names[0]} and {names[1]} like this'
#         case 3:
#             return f'{names[0]}, {names[1]} and {names[2]} like this'
#         case _:
#             return f'{names[0]}, {names[1]} and {count} others like this'

# alternative solution #1
# def likes(names):
#     match names:
#         case []: return 'no one likes this'
#         case [a]: return f'{a} likes this'
#         case [a, b]: return f'{a} and {b} like this'
#         case [a, b, c]: return f'{a}, {b} and {c} like this'
#         case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'

# alternative solution #2
def likes(names):
    formats = {
            0: "no one likes this",
            1: "{} likes this",
            2: "{} and {} like this",
            3: "{}, {} and {} like this",
            4: "{}, {} and {others} others like this"
        }
    n = len(names)
    return formats[min(n,4)].format(*names, others=n-2)


# arr = likes([])
# arr = likes(["Peter"])
# arr = likes(["Jacob", "Alex"])  
# arr = likes(["Max", "John", "Mark"])
# arr = likes(["Alex", "Jacob", "Mark", "Max"])
arr = likes(["Alex", "Jacob", "Mark", "Max", "Elise"])

print(arr)
