# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:

# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

# orginial
# def descending_order(num):
#     num_str = str(num)
#     num_list = []
#     for n in num_str:
#         num_list.append(n)
#         num_list.sort(reverse=True)
#     num_list = ''.join(num_list)
#     return int(num_list)

# refractored
# def descending_order(num):
#     num = str(num)
#     lst = [num[i] for i in range(0, len(num))]
#     lst.sort(reverse=True)
#     lst = ''.join(lst)
#     return int(lst)

# clever solution
def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))

num_input = descending_order(42145)
# num_input = descending_order(145263)
# num_input = descending_order(123456789)

print(num_input, type(num_input))