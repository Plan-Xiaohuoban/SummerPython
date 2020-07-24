

# print(61.5 >= 60)  # True
# print(61.5 == 60)  # False
# print(61.5 <= 60)  # False

# if-else
score = 61.5
if score >= 60:
    grade = "P"
else:
    grade = "F"
    print(grade)

# # if-else-if
# if score == 100:
#     grade = "A+"
# elif score >= 95:
#     grade = "A"
# else:
#     grade = "A-"
# print(grade)


if score == 100:
    grade = "A+"
elif score >= 95:
    grade = "A"
elif score >= 90:
    grade = "A-"
elif score >= 85:
    grade = "B+"
elif score >= 80:
    grade = "B"
elif score >= 77:
    grade = "B-"
elif score >= 73:
    grade = "C+"
elif score >= 70:
    grade = "C"
elif score >= 67:
    grade = "C-"
elif score >= 63:
    grade = "D+"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
