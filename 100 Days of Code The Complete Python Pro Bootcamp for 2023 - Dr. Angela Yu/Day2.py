#Day 2.

#Data Types, Numbers, Operations, Type Conversion, f-Strings.

#Python Primitive Data Types.

'''
print(len(12345)) -> Type error. 
Index. 
Subscripting - Method of pulling out a particular element from a string is called subscripting. 
Integer. Large Integers instead of commas, we will put underscores. 
Float or Floating Point Number. 
Boolean - True or False. 
''' 
print("Hello"[0])
print("Hello"[4])
print("Hello"[-1])
print("123" + "345")
print(123 + 345)
print(123_456_789)
print(3.14)

#Type Error, Type Checking and Type Conversion. 

'''
len function doesn't work with integers. 

num_char = len(input("What is your name?"))
print("Your name has " + num_char + " characters.")
This gives us a error.

type() function -> Helps us see what data type it is. 
Type conversion or type casting. 
str().

'''
num_char = len(input("What is your name?"))
print(type(num_char))

num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a))

a = str(123)
print(type(a))

a = float(123)
print(type(a))

print(70 + float(100.5))

a = print(70 + float(100.5))
print(type(a))
#<class 'NoneType'>. 
#NoneType -> is a data type that simply shows that an object has no value/has a value of None .

print(str(70) + str(100))

#[Interactive Coding Exercise] Data Types.
two_digit_number = input("Type a two digit number: ")
type(two_digit_number)
a = int(two_digit_number[0])
b = int(two_digit_number[1])
print(a+b) 

#The above is my solution to the problem. 
#Answer:
two_digit_number = input("Type a two digit number: ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)

#Mathematical Operations in Python. 

'''
3+5 7-4 3*2 6/3 2**3 
PEMDAS - Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction. 
() ** * / + -
'''
print(3*3+3/3-3)
print(3/3*3+3-3)
print(3*(3+3)/3-3)

#[Interactive Coding Exercise] BMI Calculator.
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
a = float(height)
b = float(weight)
BMI = b / (a**2)
print(int(BMI))

#The above is my solution to the problem. 
#Answer:
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

#Number Manipulation and F Strings in Python.

'''
round function. floor division.
+= or -= or /= or *=  
F strings -> mix strings and different data types. 
'''
print(round(8/3))
print(round(8/3, 2))
print(round(2.66666666, 2))
print(8//3)
print(type(8//3))
print(type(8/3))

result = 4/2
result / 2
print(result)

score = 0 
score+=1
print(score)

score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#[Interactive Coding Exercise] Life in Weeks. 
age = input("What is your current age? ")
days_left = 365 * (90 - (int(age))) 
weeks_left = 52 * (90 - (int(age))) 
months_left = 12 * (90 - (int(age))) 
print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left. ")

#The above is my solution to the problem. 
#Answer:
age = input("What is your current age? ")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = (f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left.")
print(message)

#Day 2 Project: Tip Calculator. 
print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")
tip_percentage = float(tip) / 100
float(bill) * float(tip_percentage)
total_split =  ((float(bill) / float(split)) *1 * float(tip_percentage))
round(total_split)
total_split_str = str(round(total_split,2)) 
amount_total = (float(bill) / float(split)) + float(total_split)
amount_total_str = str(round(amount_total ,2))
print("Each person should pay - tip : " + (total_split_str))
print("Each person should pay totally : " + (amount_total_str))

#The above is my solution to the problem. 
#Answer:
print("Welcome to the tip calculator.")
bill = float(input("What was the the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people 
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amount}")
#{:.2f}format for rounding off. 


#This is the end of the section.


