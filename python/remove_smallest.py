# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

# Don't change the order of the elements that are left.

# Examples

# * Input: [1,2,3,4,5], output= [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]

# original attempt
# def remove_smallest(numbers):
#     arr = numbers.copy()
#     if numbers == []:
#         return []
#     else:
#         min_num = min(arr)
#         arr.remove(min_num)
#         return arr

# refractored
def remove_smallest(numbers):
    arr = numbers.copy()
    if arr:
        arr.remove(min(arr))
    return arr

# arr = remove_smallest([1,2,3,4,5]); # output= [2,3,4,5]
# arr = remove_smallest([5,3,2,1,4]) # output = [5,3,2,4]
# arr = remove_smallest([2,2,1,2,1]) # output = [2,2,2,1]
arr = remove_smallest([255, 391, 59, 178, 194, 350]) # output = [255, 391, 178, 194, 350]
# arr = remove_smallest([]) # output = []

print(arr)