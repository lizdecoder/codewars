# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

# Return True if yes, False otherwise :)

# orginal attempt
# def hero (bullets, dragons):
#     return True if bullets/2 >= dragons else False

# refractored
def hero (bullets, dragons):
    return bullets/2 >= dragons

# survive = hero(10, 5) #True
# survive = hero(7, 4) #False
survive = hero(4, 5) #False
# survive = hero(100, 40) #True

print(survive)