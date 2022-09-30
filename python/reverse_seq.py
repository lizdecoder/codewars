# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]

# original attempt
# def reverse_seq(n):
#     arr = []
#     for num in range(n+1):
#         print(num)
#         if num > 0:
#            arr.append(num)
#     arr.reverse()
#     return arr

# clever solutions
# def reverse_seq(n):
#     return [num for num in range(n, 0, -1)]

def reverse_seq(n):
    # a list of 3 to 0, with a step of -1
    return list(range(n, 0, -1))

# a = reverse_seq(5)
# a = reverse_seq(10)
a = reverse_seq(3)
# a = reverse_seq(54)
print(a)