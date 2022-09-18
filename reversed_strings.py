# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

str = 'stressed'
# original solution
# reversed = str[::-1]

# alternate solution
reversed = list(str)
reversed.reverse()
reversed = ''.join(reversed)
print(reversed)


