# Summing the last 3 (instead of 2) numbers of the sequence to generate the next.

# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:
# [1, 1 ,1, 3, 5, 9, 17, 31, ...]

# But what if we started with [0, 0, 1] as a signature? 
# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

# Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

# Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

# original attempt
# learn: while loop is less efficient
# do not need conditional for n==0
def tribonacci(signature, n):
    for i in range(n):
        next_element = sum(signature[-3:])
        signature.append(next_element)
    return signature[:n]


result = tribonacci([1, 1, 1], 0)
# result = tribonacci([1, 1, 1], 10)
# result = tribonacci([1, 2, 3], 10)
# result = tribonacci([1, 1, 1], 1)
print(result)