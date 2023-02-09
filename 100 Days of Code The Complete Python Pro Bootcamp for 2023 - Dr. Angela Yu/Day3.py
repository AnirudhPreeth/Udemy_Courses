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



    

 