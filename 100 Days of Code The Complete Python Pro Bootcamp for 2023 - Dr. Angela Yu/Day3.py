#Day 3. 

#Control Flow and Logical Operators. 

#Control Flow with if / else and Conditional Operators.

'''
If/else.
if condition:
  do this
else: 
  do this
Flowchart. draw.io
Comparison Operators : > < >= <= == !=
Modulo (%).

'''
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the rollercoaster!")
else: 
    print("Sorry, you have to grow taller before you can ride!")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
else: 
    print("Sorry, you have to grow taller before you can ride!")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height == 120:
    print("You can ride the rollercoaster!")
else: 
    print("Sorry, you have to grow taller before you can ride!")

#[Interactive Coding Exercise] Odd or Even? Introducing the Modulo.
number = int(input("Which number do you want to check? "))
if (number%2) == 0:
    print("This is an even number.")
else: 
    print("This is an odd number.")

#The above is my solution to the problem. 
#Answer:
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else: 
    print("This is an odd number.")

#Nested if statements and elif statements.

'''
Nested if/else statement. 
if condition:
  if another condition:
    do this
  else:
    do this
else:
  do this
  
elif condition. 
if condition1:
  do A
elif condition2:
  do B
else:
  do this  
'''
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age<=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")    
else: 
    print("Sorry, you have to grow taller before you can ride!")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age<=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")    
else: 
    print("Sorry, you have to grow taller before you can ride!")

#[Interactive Coding Exercise] BMI 2.0.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / (height ** 2))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
            
#The above is my solution to the problem. 
#Answer:
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
          
#[Interactive Coding Exercise] Leap Year.             

year = int(input("Which year do you want to check? "))
if year %4 == 0 and year %400 == 0 and year %100 != 0:
    print("Leap Year.")
else: 
    print("Not a Leap Year.")

year = int(input("Which year do you want to check? "))
if year %4 == 0 and year %400 == 0 or year %400 != 0:
    print("Leap Year.")
    if year %100 == 0:
        print("Not Leap year.")
else: 
    print("Not Leap Year.")
        
        
year = int(input("Which year do you want to check? "))
if year %4 == 0 and year %400 == 0 or year %4 == 0 and year %400 !=0:
    print("Leap Year.")
    if year %100 == 0 and year%4 == 0 and year%400 != 0:
        print("Not Leap year.")
        if year %100 !=0 and year %4 == 0 and year %400 !=0:
            print("Not Leap Year.")
else: 
    print("Not Leap Year.")
            
#The above is my solution to the problem. 
#In the above, I documented my various test cases. 
#In the last one, almost every year gave the right answer, except 2100. 
#While the test case accepted the answer and it was a 100 per cent correct according to the test cases it used, it didn't use 2100. 
#I'm not satisfied, and will check back on it later. 
#Answer:
year = int(input("Which year do you want to check? "))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap Year.")
        else:
            print("Not leap year.")
    else:
        print("Leap Year.")
else:
    print("Not leap year.")
    
#Multiple If Statements in Succession.

'''
Multiple if.
if condition1:
  do A
if condition2:
  do B
if condition3:
  do C
 
bill = bill + 3 is the same as bill +=3.  
'''
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age<=18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")    
    
    wants_photos = input("Do you want a photo taken? Y or N.")
    if wants_photos == "Y":
        bill += 3  
    print(f"Your final bill will be: ${bill}.")                  
else: 
    print("Sorry, you have to grow taller before you can ride!")

#[Interactive Coding Exercise] Pizza Order Practice.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill = +15
elif size == "M":
    bill = +20
else:
    bill = +25
if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill+=3
    
if extra_cheese == "Y":
    bill+=1
print(f"Your final bill is: {bill}.")

#The above is my solution to the problem.
#Answer:
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill = +15
elif size == "M":
    bill = +20
else:
    bill = +25
    
if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill+=3
    
if extra_cheese == "Y":
    bill+=1
print(f"Your final bill is: {bill}.")

#Logical Operators.

'''
Logical Operators. And, Or and Not. 
A and B. 
When you combine two different conditions using an And operator, they both have to be true. 
For the entire line of code. If just one of them is true, say A is true and B is false or vice versa, overall thing is false. 
C or D.
Or needs only condition to be true. If one of them is true, they both evaluate to true. 
Only when both C or D are false does the statement actually become false. 
not E.
This basically reverses a condition. 
If condition is false, it becomes true, if it's true it becomes false.
'''
 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age<=18:
        bill = 7
        print("Youth tickets are $7.")
    elif age>=45 and age<=55:
        bill = 12
        print("Everything is going to be okay. Have a free ride on us!")       
    else:
        bill = 12
        print("Adult tickets are $12.")   
    wants_photos = input("Do you want a photo taken? Y or N.")
    if wants_photos == "Y":
        bill += 3  
    print(f"Your final bill will be: ${bill}.")                  
else: 
    print("Sorry, you have to grow taller before you can ride!")    

'''
lower() function. 
count() function. Count() function is case sensitive. 
'''
#[Interactive Coding Exercise] Love Calculator.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
both_names = name1 + name2
lower_case = both_names.lower()
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
true_score = t+r+u+e
l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
love_score = l+o+v+e
total_score = int(str(true_score) + str(love_score))
if (total_score < 10) or (total_score > 90):
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif (total_score >= 40) and (total_score <=50):
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}")  
          
#The above is my solution to the problem.
#Answer:

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_string = name1 + name2
lower_case_string = both_names.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t+r+u+e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l+o+v+e
love_score = int(str(true_score) + str(love_score))
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <=50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")  
    
#Day 3 Project: Treasure Island. 

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
