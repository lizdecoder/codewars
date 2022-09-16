# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

name = input("Enter your name? " )

def greeting(name):
	return f"Hello, {name} how are you doing today?"

print(greeting(name))