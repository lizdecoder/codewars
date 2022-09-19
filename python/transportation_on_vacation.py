# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

# Write a code that gives out the total amount for different days(d).

# original attempt
# initialCost = 40
# d = 1

# def transportationCost(d):
# 	if d >= 7:
# 		total = (initialCost*d) - 50
# 	elif d >= 3:
# 		total = (initialCost*d) - 20
# 	else:
# 		total = initialCost*d
# 	return total

# clever solution
def rental_car_cost(d):
    return 40 * d - ((50, 20)[d < 7], 0)[d < 3]

cost = rental_car_cost(2)
print(cost)
