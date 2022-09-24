# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

# original attempt
# def bmi(weight, height):
# 	measurement = weight/(height**2)
# 	if measurement <= 18.5:
# 		return "Underweight"
# 	elif measurement <= 25.0:
# 		return "Normal"
# 	elif measurement <= 30.0:
# 		return "Overweight"
# 	else:
# 		return "Obese"

# clever solution
def bmi(weight, height):
	index = weight/ (height**2)
	return ['Underweight', 'Normal', 'Overweight', 'Obese'][(index > 30) + (index > 25) + (index > 18.5)]

# body_measurement = bmi(50,1.80)
# body_measurement = bmi(80,1.80)
# body_measurement = bmi(90,1.80)
# body_measurement = bmi(110,1.80)
body_measurement = bmi(50,1.50)
print(body_measurement)