# Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

# The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

# two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]

# original attempt
# def two_sum(numbers, target):
#     arr = {}
#     for i, num in enumerate(numbers):
#         print(i, num)
#         if target - num in arr:
#             print("in")
#             print(f'in again: {target-num, i}')
#             return [arr[target-num], i]
#         arr[num] = i

# refractored
def two_sum(numbers, target):
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if i != j and x + y == target:
                return [i, j]

# idx = two_sum([1,2,3], 4) #[0,2]
# idx = two_sum([1234,5678,9012], 14690) #[1,2]
idx = two_sum([2,2,3], 4) #[0,1]
print(idx)