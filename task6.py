'''text = input("Enter sentence: ")
print("Upper       :", text.upper())
print("Lower       :", text.lower())
print("Title       :", text.title())
print("Capitalized :", text.capitalize())
print("Swap case   :", text.swapcase())

if text.isupper():
    print("Original text is uppercase")
elif text.islower():
    print("Original text is lowercase")
elif text.istitle():
    print("Original text is title case")
else:
    print("Original text has mixed case")
    '''
'''#username
while True:
    username = input("Enter username: ")

    if username == "quit":
        break

    if username.isidentifier():
        print("Valid Python identifier")
    else:
        print("Not a valid Python identifier")

    if username.isascii():
        print("Contains only ASCII characters")
    else:
        print("Contains non-ASCII characters")

    if username[0].isalpha():
        print("Begins with a letter")
    else:
        print("Does not begin with a letter")

    if username.isalnum():
        print("Contains only letters and numbers")
    else:
        print("Does not contain only letters and numbers")
'''
#student report
students = []
for i in range(3):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    if marks < 0 or marks > 100:
        print("Invalid marks")
        continue
    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"
    students.append((name, marks, grade))
print("=" * 40)
print("STUDENT REPORT".center(40))
print("=" * 40)
print(f"{'Name'.ljust(15)} {'Marks'.rjust(8)} {'Grade'.rjust(8)}")
print("-" * 40)
for name, marks, grade in students:
    print(f"{name.ljust(15)} {str(marks).rjust(8)} {grade.rjust(8)}")
print("=" * 40)
#: Character and Text Analyser
text = input("Enter a line of text: ")

letters = 0
digits = 0
spaces = 0
printable = 0
non_printable = 0

for ch in text:
    if ch.isalpha():
        letters += 1

    if ch.isdigit():
        digits += 1

    if ch.isspace():
        spaces += 1

    if ch.isprintable():
        printable += 1
    else:
        non_printable += 1
print("\n--- Text Analysis ---")
print(f"Letters       : {letters}")
print(f"Digits        : {digits}")
print(f"Spaces        : {spaces}")
print(f"Printable     : {printable}")
print(f"Non-printable : {non_printable}")
print(f"Lower case    : {text.islower()}")
print(f"Upper case    : {text.isupper()}")
print(f"Title case    : {text.istitle()}")














