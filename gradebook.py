# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'

# def grade(grade1, grade2, grade3):
# 	average = (grade1+grade2+grade3)/3
	# letterGrade = ""
	# print(average)
	# match letterGrade:
	# 	case 100:
	# 		letterGrade = "A"
	# 	case 90:
	# 		letterGrade = "B"
	# 	case 80:
	# 		letterGrade = "C"
	# 	case 70:
	# 		letterGrade = "D"
	# 	case _:
	# 		letterGrade = "F"
	# return letterGrade
	# if(average >= 90):
	# 	letterGrade = "A"
	# elif (average >= 80):
	# 	letterGrade = "B"
	# elif (average >= 70):
	# 	letterGrade = "C"
	# elif (average >= 60):
	# 	letterGrade = "D"
	# else:
	# 	letterGrade = "F"
	# return letterGrade

# clever solution
def get_grade(*s):
    match sum(s) // 30:
        case 10 | 9: return 'A'
        case 8: return 'B'
        case 7: return 'C'
        case 6: return 'D'
    return 'F'

grade1 = 100
grade2 = 99
grade3 = 89


avg = get_grade(grade1, grade2, grade3)
print(avg)