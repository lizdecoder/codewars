# Given an integral number, determine if it's a square number:

# The tests will always use some integral number, so don't worry about that in dynamic typed languages.

# Examples
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false


import math

#original solution
# def is_square(n):
#     if n < 0:
#         return False
#     num = math.sqrt(n)
#     return True if num*num == n else False

#clever solution
def is_square(n):
    # is_interger() returns boolean if sqrt(n) is a whole number
    return False if n < 0 else math.sqrt(n).is_integer()


# bool = is_square(-1)
# bool = is_square(0)
# bool = is_square(3)
# bool = is_square(4)
# bool = is_square(25)
bool = is_square(26)

print(bool)