print("Student Grade Calculator")

name = input("Student name: ")
midterm = float(input("Midterm exam score: "))
final = float(input("Final exam score: "))

average = (midterm * 0.4) + (final * 0.6)

print("Average score:", average)

if average >= 50:
    print("Result: Passed")
else:
    print("Result: Failed")


