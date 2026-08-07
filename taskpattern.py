'''# write a python program to caluculate the innings of a batsman  and count the total score,dot balls,boundaris
runs=[4,6,1,0,2,4,0,6]
total_score=dot_balls=0
boundaries=0
for run in runs:
    total_score = total_score + run

    if run == 0:
        dot_balls = dot_balls + 1

    if run == 4 or run == 6:
        boundaries = boundaries + 1

print("Total Score:", total_score)
print("Dot Balls:", dot_balls)
print("Boundaries:", boundaries)
'''
'''#While loop
#write a python program for phone pattern
#Account locked....
password="1234"
max_attempts=5
current_attempt=0
while current_attempt < max_attempts:
    entered_password=input("enter the pssword:")
    if entered_password==password:
        print("unlocked")
    else:
        print("Entered Password is wrong...try again carefully")
        current_attempt +=1
else:
    print("password Locked,try after 30 sec...")
'''
'''#movies
movies=["salaar","bahubali","KGF"]
print("Move List:")
for movie in movies:
    print(movie)
'''
#ATM pin
password="1234"
max_attempts=3
current_attempt=0
while current_attempt < max_attempts:
    entered_password=input("enter the pssword:")
    if entered_password==password:
        print("unlocked")
    else:
        print("Entered Password is wrong...try again carefully")
        current_attempt +=1
else:
    print("password Locked,try after 30 sec...")


        
