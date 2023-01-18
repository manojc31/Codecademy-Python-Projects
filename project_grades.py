def grade_converter(grade):
    if grade >=90:
        return "A"
    elif grade < 90 and grade >= 80:
        return "B"
    elif grade < 80 and grade >= 70:
        return "C"
    elif grade <70 and grade >= 65:
        return "D"
    else:
        return "F"

print(grade_converter(92))
print(grade_converter(70))
print(grade_converter(61))