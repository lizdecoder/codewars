# Given a non-empty array of integers, return the result of multiplying the values together in order. Example: [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

arr = [1, 2, 3, 4] # 1 * 2 * 3 * 4 = 24
# arr = [4, 1, 1, 1, 4] #should be 16
# arr = [2, 2, 2, 2, 2, 2]  #should be 64


def grow(arr):
	total = 1
	for num in arr:
		total *= num
	return total

num = grow(arr)
print(num)