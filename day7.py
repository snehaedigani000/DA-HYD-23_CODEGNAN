'''work_log=[0,1,1,1,0,1,0]
#result variable --> longest_streak
longest_streak =0 #target variable
current_streak=0
for day in work_log:
    if day==1:
        #print(day)
        current_streak=current_streak+1
        if current_streak > longest_streak:
            longest_streak=current_streak
            print(longest_streak)
        
    else:
        current_streak=0#streak breaks
else:
    print(f'Longest Streak is (longest_streak)')
#in this case when the entire loop execution is doe we get result of
#else block

'''
'''#notification=[0,0,0,]
#for-else with notifications scenario
#try to take notificatios from user-->ist of Integers
notifications = list(map(int,input("Enter the values-->0 or 1:").split(',')))
print(notifications)
for notification in notifications:
    if notification==1:
        print('Unread Notifiction')
        break
else:
    print('All caught Up')
#while-->it relise on Condition,it will be completely executed until the
#Conditon is satisfied...
'''
'''syntax while:

while<condition>:
       statement(s)...
       .....
       .....
'''
'''while True:
    print("Yes")
'''
'''#It runs an infinite loop e need to click ctrl+c(Keybord interrupt)
i=0#initialised satement
while i<=10:
    print(i)
    i=i+1#Counter
'''
'''i = 10
while i >= 1:
    print(i)or#print(10-i)
    i= i-1    
'''
#banking scenrio-->PIN authenticatin if more 3 attempts
#Account locked..
pin="2612"
max_attempts=3
current_attempts=0
while current_attempts<=max_attempts:
    entered_pin=input("Enter the ATM PIN:")
    if entered_pin==pin:
        print("Login Successful")
        break
    else:
        print("Entered PIN is wrong..Try again carefully")
        current_attempts+=1
else:
    print("Accout Locked,try after 24hours..")
        
    
        
          
    
