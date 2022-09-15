# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

name = 'Robert'
# name = "Elise"
# name = "Ginger"

# my original solution
# def banjo(name):
# 	if name[0] == ("r") or name[0] == ("R") :
# 		return name + " plays banjo"
# 	else:
# 		return name + " does not play banjo"

# Alternate solution
# def banjo(name):
# 	if name[0].lower().startswith('r'):
# 		return name + " plays banjo"
# 	else:
# 		return name + " does not play banjo"

def banjo(name):
	return name + (" does not play banjo", " plays banjo") [name[0].lower() == 'r']

plays = banjo(name)
print(plays)
