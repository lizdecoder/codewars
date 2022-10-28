# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

# Examples

# Valid arrays

# a = [121, 144, 19, 161, 19, 144, 19, 11]  
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

# a = [121, 144, 19, 161, 19, 144, 19, 11] 
# b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

# Invalid arrays

# If, for example, we change the first number to something else, comp is not returning true anymore:

# a = [121, 144, 19, 161, 19, 144, 19, 11]  
# b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
# comp(a,b) returns false because in b 132 is not the square of any number of a.

# a = [121, 144, 19, 161, 19, 144, 19, 11]  
# b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
# comp(a,b) returns false because in b 36100 is not the square of any number of a.

# original attempt
# def comp(array1, array2):
#     arr = []
#     if array1 is None or array2 is None:
#         return False
#     for num in array1:
#         arr.append(num**2)
#     arr.sort()
#     array2.sort()
#     if arr == array2:
#         return True
#     return False

# refractored original to remove additional array
def comp(array1, array2):
    return array1 != None and array2 != None and sorted([i ** 2 for i in array1]) == sorted(array2)
            
# clever attempt
# def comp(array1, array2):
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False

#test 1
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

# bool = comp(a1, a2) #true

#test 2
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

# bool = comp(a1, a2) #false

#test 3
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]

# bool = comp(a1, a2) #false

#test 4
a1 = []
a2 = None

bool = comp(a1, a2) #False

print(bool)