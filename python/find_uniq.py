# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# do not use for loop for large arrays
# def find_uniq(arr): 
#     for num in arr:
#         if arr.count(num) == 1:
#             return num

# refractored for large arrays
# def find_uniq(arr):    
#     arr.sort()
#     if arr[0] != arr[len(arr)-1]:
#         if arr[0] == arr[len(arr)-2]:
#             return arr[len(arr)-1]
#         return arr[0]

# refractored again...
def find_uniq(arr):
    arr.sort()
    return arr[0] if arr[0] != arr[1] else arr[-1]

# clever attempt
# def find_uniq(arr):   
#     a, b = set(arr)
#     return a if arr.count(a) == 1 else b

# clever attempt 2
# def find_uniq(arr): 
    # by add [0] at the end, you return the value and not an array with the value
    # return [x for x in set(arr) if arr.count(x) == 1][0]


# unique = find_uniq([ 1, 1, 1, 2, 1, 1 ]) # 2
# unique = find_uniq([ 0, 0, 0.55, 0, 0 ]) # 0.55
unique = find_uniq([4, 4, 4, 3, 4, 4, 4]) # 3
print(unique)