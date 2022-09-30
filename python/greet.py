# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

# Use conditionals to return the proper message:

# case	return
# name equals owner	'Hello boss'
# otherwise	'Hello guest'

def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'

response = greet('Daniel', 'Daniel')
# response = greet('Greg', 'Daniel')
print(response)