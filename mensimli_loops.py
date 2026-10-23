# Q1
for i in range(10,0,-1):
    print(i)
print('Liftoff!')


# Q2
childTicket=0
adultTicket=0
for i in range(1,6):
    visitorAge=int(input('Enter your age: '))
    if visitorAge<18:
        childTicket=childTicket+1
    else:
         adultTicket=adultTicket+1
print('Child ticket: ',childTicket)
print('Adult ticket: ',adultTicket)


# Q3
for i in range(1, 10, 2):
    print(i, end=" ") 
# 1 3 5 7 9 

# Q4
total=0
number=5
for i in range(number):
    priceItem=float(input('Enter the price'))
    total=total+priceItem
print('Total: ',total)
print('Average: ',total/number)

# Q5
while True:
    newPassword=input('Enter new password: ')
    if len(newPassword)<8:
        print("Too short, try again")
    else:
        print("Password accepted")
        break
    
# Q6
balance = 100 
while balance > 0:
    balance -= 30 
    print(balance)
print("Done")
# 70 40 10 -20 Done

# Q7
record=0
day=0
for i in range(7):
    record+=1200
    day+=1
    print('Day',day,": ",record)
    
# Q8
correctUsername='admin'
correctPassword="1234"
attempts=0
while attempts<3:
       username=input('Enter username: ')
       password=input('Enter password: ')
       if username==correctUsername and password==correctPassword:
          print("Welcome!")
          break
       else:
        attempts+=1
        print('Wrong username or password ')
if attempts==3:
       print("Account locked")
       
# Q9
balance=500
while True:
    amount=float(input("How much do you want to withdraw? "))
    if balance==0:
        print("Goodbye")
        break
    elif amount<0:
        print('Invalid amount')
    elif balance<amount:
        print("Insufficient funds")
    else:
        balance-=amount
        print('New balance: ',balance)
        

# Q10
pin = "1234"
attempts = 0
while attempts < 3:
    entered = input("PIN: ") 
    attempts += 1    
    if entered == pin:
     print("Access granted")
     break 
    print("Wrong PIN,", 3 - attempts, "attempts left")
print("Attempts used:", attempts) 
# Wrong PIN  2 attempts left
# Wrong PIN  1 attempts left
# Access granted
# Attempts used: 3

# Q11
highest=0
passed=0
failed=0
total=0
while True:
    grade=float(input('Enter the grade: '))
    if grade==-1:
        break
    if grade>=51:
        passed+=1
    else:
        failed+=1
    if grade>highest:
        highest=grade
    total+=grade
average=total/(passed+failed)
print('Passed: ',passed)
print('Failed: ',failed)
print('Highest: ',highest)
print('Average: ',round(average, 1))


# Q12
freespaces = 20
while True:
    command = input('Enter command.IN,OUT,STOP: ')
    match command:
        case 'IN':
            if freespaces == 0:
                print("Garage full")
            else:
                freespaces -= 1
                print('Free space: ',freespaces)
        case 'OUT':
            if freespaces == 20:
                print("Garage is empty")
            else:
                freespaces += 1
                print('Free space: ',freespaces)
        case 'STOP':
            break
        case _:
            print('Unknown command')

# Q13
hottestDegree=0
hotDays=0
day=0
for i in range(7):
    day+=1
    degree=int(input('Enter degree: '))
    if degree>30:
        hotDays+=1
    if degree>hottestDegree:
        hottestDegree=degree
        hottestDay=day
    print('Day',day,': ',degree)
print('Hot days: ',hotDays)
print('Hottest day: ',hottestDay)
    
# Q14
password = "secret" 
attempts = 0
while True: 
    entered = input("Password: ") 
    if entered == password: 
          print("Welcome") 
          break
    attempts += 1 
    if attempts == 3: 
        print("Account locked")
        break 
# Having attempts=0 inside while caused the program to malfunction bc attempts was reset to zero every time the loop repeated


# Q15
while True:
    password=input('Enter teh password: ')
    if len(password)<8:
        print('Weak password: lengh should be at least 8 characters')
    elif password.isdigit():
        print('Weak password: digits should also be used')
    elif password.isupper():
        print('Weak password: at least 1 lowercase letter should also be used')
    elif password.islower():
        print('Weak password: at least 1 uppercase letter should also be used')
    else:
        print('Strong password')
        break
    
# Q16
balance=0
month=0
save=50
while balance<1000:
    month+=1
    balance+=save
    print('Month',month,': ',balance)
    save+=10
print("Goal reached in month",month)  

# Q17
number = 100
while True: 
        number += 1 
        if number % 7 == 0 and number % 2 == 1: 
            break
print(number)
# This program finds the first number which is odd nad completely divides by 7 without remainder above 100
# break helps stop the loop when it finds the number

# Q18
correctPin='2580'
balance=1000
attempts=0
while True: 
    pin=input("Password: ") 
    if pin==correctPin: 
        while True:
            menu=input('Menu: (1-Check balance,2-deposit,3-withdraw,4-exit)')
            match menu:
                case '1':
                    print('Balance: ',balance)
                    continue
                case '2':
                    amount=float(input('Enter the amount'))
                    if amount>0:
                        balance+=amount
                    continue
                case '3':
                    amount=float(input('Enter the amount'))
                    if amount>0:
                        balance-=amount
                    continue
                case '4':
                    print('Goodbye')
                    break
                case _:
                    print('Invalid choice')
                    continue
        break
    attempts += 1 
    if attempts == 3: 
        print("Account locked")
        break 
  
  
# Q19
total=0
cost=1.5
while total<cost:
    coin=float(input('Enter the coin.(0.05,0.10,0.20,0.50,1)'))
    match coin:
        case 0.05:
            total+=coin
            print('Total: ',round(total, 2) )
            continue
        case 0.10:
            total+=coin
            print('Total: ',round(total, 2) )
            continue
        case 0.20:
            total+=coin
            print('Total: ',round(total, 2) )
            continue
        case 0.50:
            total+=coin
            print('Total: ',round(total, 2) )
            continue
        case 1:
            total+=coin
            print('Total: ',round(total, 2) )
            continue
        case _:
            print("Coin not accepted")
            continue
changes=total-cost
print('Here is your water')
print('Changes:',round(changes,2))


# Q20
count=0
for num in range(2,101):
    prime=True
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
    if prime:
        print(num,end=' ')
        count+=1
print('Total codes: ',count)
        
# Q21
for floor in range(1, 4): 
    for room in range(1, 5):
        if room == 3:
            break
        print(floor * 100 + room, end=" ")
    print() 
# 101 102
# 201 202 
# 301 302 

#Q22
for floor in range(1, 6):
    if floor == 4:
         continue
    print('Floor',floor,end=' ')
    for room in range(1, 5):
        print(floor * 100 + room, end=" ")
    print() 


# Q23
timeLeft=480
count=0
while timeLeft>0:
    customerMin=int(input('Enter minutes: '))
    if customerMin==0:
        print("The queue is empty")
        break
    if customerMin>timeLeft:
        print("Sorry, come back tomorrow")
        break
    timeLeft-=customerMin
    count+=1
print('Customers served: ',count)
print('Minutes left: ',timeLeft)

# Q24
countA=0
countB=0
countC=0
countSpoiled=0
while True:
    vote=input('Enter vote: ')
    match vote:
        case 'A':
            countA+=1
        case 'B':
            countB+=1
        case 'C':
            countC+=1
        case 'End':
            break
        case _:
            countSpoiled+=1
print('A:',countA,"B:",countB,'C:',countC)
print('Spoiled: ',countSpoiled)
if countA>countB and countA>countC:
    print('Winner: A')
elif countB>countA and countB>countC:
    print('Winner: B')
elif countC>countB and countC>countA:
    print('Winner: C')
else:
    print('Tie')
    
    
# Q25
while True:
    total=0
    cardNumber=input('Enter card number')
    if len(cardNumber)!=16:
        print("Must be 16 digits")
        continue
    if not cardNumber.isdecimal() or not cardNumber.isascii():
        print('Only digits is allowed')
        continue
    for i in range(14,-1,-2):
        doubleI=2*int(cardNumber[i])
        if doubleI>9:
            doubleI-=9
        total+=doubleI+int(cardNumber[i+1])
    if total%10==0:
        print('Valid card number')
        break
    else:
        print('Invalid card number')