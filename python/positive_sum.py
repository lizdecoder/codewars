# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

# original solution
# def positive_sum(arr):
#     sum = 0
#     for num in arr:
#         if num > 0:
#             sum += num
#     return sum

# clever solution
def positive_sum(arr):
    return sum(num for num in arr if num > 0)

# sum = positive_sum([1,-4,7,12]) #20
# sum = positive_sum([1, -2, 3, 4, 5]) #13
sum = positive_sum([-1,2,3,4,-5]) #9
print(sum)