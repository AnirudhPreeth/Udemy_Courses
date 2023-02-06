#Day 1. 

#Printing, Commenting, Debugging, String Manipulation and Variables. 

'''
print() function -> To print / output what you want to print. 
Strings -> String of characters. Double quotes. "". 
Syntax highlighting. 
'''
print("Hello World!")

#[Interactive Coding Exercise] Printing. 
#Exercise 1 - Printing. 
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#The above is my solution to the problem. 
#Answer:
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

'''
String Manipulation and Code Intelligence -
New Line -> \n.
No gaps unless space is required for new line. 
Concatenation -> Combine different strings so that they will be added to the end of another string. 
Spaces are important in Python. 
Indentation Error.  
'''
print("Hello World!\nHello World!")
print("Hello" + "Angela") 
print("Hello" + " Angela")
print("Hello " + "Angela")
print("Hello" +" "+ "Angela")

#[Interactive Coding Exercise] Debugging Practice.
#Exercise 2 - Debugging Practice.

'''
Day 1 - String Manipulation
String Concatenation is done with the "+" sign.
e.g. print("Hello " + "world")
New lines can be created with a backslash and n.
'''
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#The above is my solution to the problem. 
#Answer:
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#The Python Input Function. 
'''
Input function - 
input("A prompt for the user")
Thonny. 
input() will get user input in console.
Then print() will print the word "Hello" and the user input. 
'''
print("Hello " + input("What is your name?") + "!")

#[Interactive Coding Exercise] Input Function. 
#Exercise 3 - Input Function.
s = print(input("What is your name? "))
print(len(s))

#The above is my solution to the problem. 
#Answer:
print(len(input("What is your name? ")))

#Python Variables. 
name = input("What is your name?")
print(name)
name = "Jack"
print(name)
name = "Angela"
print(name)

name = input("What is your name?")
length = len(name)
print(length)

#[Interactive Coding Exercise] Variables.
#Exercise 4 - Variables. 
variable1 = input("a: ")
variable2 = input("b: ")
temp = variable1
variable1 = variable2
variable2 = temp
print("a: " + variable1)
print("b: " + variable2)

#The above is my solution to the problem. 
#Answer:
a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)

#Variable Naming.
'''
No spaces between the names. Only underscores. 
'''

#Day 1 Project: Band Name Generator.

#1. Create a greeting for your program.
a = print(input("Welcome to the Band Name Generator."))
#2. Ask the user for the city that they grew up in.
b = print(input("What's name of the city you grew up in?"))
#3. Ask the user for the name of a pet.
c = print(input("What's your pet's name?"))
#4. Combine the name of their city and pet and show them their band name.
print("You band name could be " + b + " " + c)
#5. Make sure the input cursor shows on a new line:

#The above is my solution to the problem. 
#Answer:
print("Welcome to the band name generator.")
city = input("Which city did you grow in?\n")
pet = input("What is the name of a pet?\n")
print("Your band name could be " + city + " " + pet)


#This is the end of the section.