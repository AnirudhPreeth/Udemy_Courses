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

 