# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):    
    # for i in range(len(arr)):
    #     count = arr.count(arr[i])
    #     if count == 1:
    #         return arr[i]

    for num in arr:
        if arr.count(num) == 1:
            return num

# unique = find_uniq([ 1, 1, 1, 2, 1, 1 ]) # 2
unique = find_uniq([ 0, 0, 0.55, 0, 0 ]) # 0.55
print(unique)