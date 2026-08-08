'''#pyhon program to secret code using whil loops
secret_pin = 1234
pin = int(input("Enter your PIN: "))
while pin!= secret_pin:
    print("Incorrect PIN. Try again.")
    pin = int(input("Enter PIN: "))
print("Correct PIN!")
'''
'''#OTP VERIFICATION
otp="1234"
max_attempts=7
current_attempt=0
while current_attempt < max_attempts:
    entered_otp=input("enter the otp:")
    if entered_otp==otp:
        print("unlocked")
    else:
        print("Entered otp is wrong...try again carefully")
        current_attempt +=1
else:
    print("otp failed,try after 30 sec...")
'''
'''secret=1234
guess=int(input("Enter pin:"))
while guess!=secret:
    if guess<secret:
        print("too low")
        guess=int(input("Enter pin:"))
    else:
        print("too high")
        guess=int(input("Enter pin:"))
else:
    print("correct guess")
'''
'''#food orders
food=input("Enter the items:")
count=0
while food!="exit":
    count+=1
    food=input("Enter the items:")
print("Total no of items ordered",count)
'''
secret="python"
current=0
max_attempts=3
while current<max_attempts:
    a=input("enter the secret:")
    if (a==secret):
        print("access access")
        break
    else:
        remaining=max_attempts-current
        print(f"Wrog Guess & you have only",remaining)
        current+=1
else:
        print("Chance over")
    

    

