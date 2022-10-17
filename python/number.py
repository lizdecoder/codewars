# There is a bus moving in the city, and it takes and drop some people in each bus stop.

# You are provided with a list (or array) of integer pairs. Elements of each pair represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop.

# Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D

# Take a look on the test cases.
# Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative.

# The second value in the first integer array is 0, since the bus is empty in the first bus stop.

# original attempt
# def number(bus_stops):
#     on_bus = 0
#     off_bus = 0
#     for stops in bus_stops:
#         on_bus += stops[0]
#         off_bus += stops[1]
#     return on_bus - off_bus

# clever solution
# def number(bus_stops):
#     return sum([stop[0] - stop[1] for stop in bus_stops])

# clever solution
def number(bus_stops):
    return sum(on - off for on, off in bus_stops)

people = number([[10,0],[3,5],[5,8]]) #5
# people = number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]) #17
# people = number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) #21

print(people)