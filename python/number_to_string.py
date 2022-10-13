# We need a function that can transform a number (integer) into a string.

# What ways of achieving this do you know?

# Examples (input --> output):

# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

def number_to_string(num):
    return str(num)

# s = number_to_string(123)
# s = number_to_string(999)
s = number_to_string(-100)
print(s, type(s))