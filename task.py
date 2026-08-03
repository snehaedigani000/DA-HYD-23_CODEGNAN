'''#marks
marks = int(input("Enter marks: "))
if marks > 100:
    print("Invalid marks entered")
elif marks >= 90 and marks <= 100:
    print("Grade: A")
    print("Remark: Outstanding!")
elif marks >= 80 and marks <= 89:
    print("Grade: B")
    print("Remark: Excellent!")
elif marks >= 70 and marks <= 79:
    print("Grade: C")
    print("Remark: Good")
elif marks >= 60 and marks <= 69:
    print("Grade: D")
    print("Remark: Fair, needs improvement")
elif marks >= 50 and marks <= 59:
    print("Grade: E")
    print("Remark: Poor, needs serious improvement")
elif marks >= 0 and marks <= 49:
    print("Grade: F")
    print("Remark: Failed, needs to reappear")
else:
    print("Invalid marks entered")
num = int(input("Enter a number: "))
'''
'''#Even or odd
num = int(input("Enter a number: "))

if num == 0:
    print("Zero is neither even nor odd")
elif num > 0 and num % 2 == 0:
    print("Positive Even Number")
elif num > 0 and num % 2 != 0:
    print("Positive Odd Number")
elif num < 0 and num % 2 == 0:
    print("Negative Even Number")
else:
    print("Negative Odd Number")
'''

