

grade_to_GPA = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 4.0,
    "B+": 3.6,
    "B": 3.3,
    "B-": 3.0,
    "C+": 2.6,
    "C": 2.3,
    "C-": 2.0,
    "D+": 1.6,
    "D": 1.3,
    "F": 0,
}

grade_GPA = {"A+": 4.0, "A": 4.0, "A-": 4.0, "B+": 3.6, "B": 3.3, "B-": 3.0}
print(grade_GPA["A-"])  # 4.0
# print(grade_GPA[3.6])
# print(grade_GPA["F"])


grade_GPA["A-"] = 3.7
print(grade_GPA)
# {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.6, 'B': 3.3, 'B-': 3.0}

grade_GPA["F"] = 0
print(grade_GPA)
# {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.6, 'B': 3.3, 'B-': 3.0, 'F': 0}
