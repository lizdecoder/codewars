# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(l):
    return [char for char in l if not isinstance(char, str)]

# fl = filter_list([1,2,'a','b'])
# fl = filter_list([1,'a','b',0,15])
fl = filter_list([1,2,'aasf','1','123',123])

print(fl)

# str = str.replace(char, "")