def get_grade(s1, s2, s3):
    grade_average =  (s1 + s2 + s3)  // 3

    if grade_average >= 90:
        return "A"
    elif 90 > grade_average >= 80:
        return "B"
    elif 80 > grade_average >= 70:
        return "C"
    elif 70 > grade_average >= 60:
        return "D"
    else:
        return "F"

print(get_grade(95, 90, 93))