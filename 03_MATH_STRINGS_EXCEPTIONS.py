# ---------- FORCE USER TO ENTER A NUMBER ----------
# By giving the while a value of True it will cycle until a break is reached
while True:

    # If we expect an error can occur surround potential error with try
    try:
        number = int(input("Please enter a number : "))
        break

    # The code in the except block provides an error message to set things right
    # We can either target a specific error like ValueError
    except ValueError:
        print("You didn't enter a number")

    # We can target all other errors with a default
    except:
        print("An unknown error occurred")

print("Thank you for entering a number")

# ---------- Problem : Implement a Do While Loop ----------
# Now I want you to implement a Do While loop in Python
# They always execute all of the code at least once and at
# the end check if a condition is true that would warrant
# running the code again. They have this format
# do {
#   ... Bunch of code ...
# } while(condition)

# I'll create a guessing game in which the user must chose
# a number between 1 and 10 of the following format
'''
Guess a number between 1 and 10 : 1
Guess a number between 1 and 10 : 3
Guess a number between 1 and 10 : 5
Guess a number between 1 and 10 : 7
You guessed it
'''

# Hint : You'll need a while and break

secret_number = 7

while True:
    guess = int(input("Guess a number between 1 and 10 : "))

    if guess == secret_number:
        print("You guessed it")
        break

# ---------- MATH MODULE ----------
# Python provides many functions with its Math module
import math

# Because you used import you access methods by referencing the module
print("ceil(4.4) = ", math.ceil(4.4))
print("floor(4.4) = ", math.floor(4.4))
print("fabs(-4.4) = ", math.fabs(-4.4))

# Factorial = 1 * 2 * 3 * 4
print("factorial(4) = ", math.factorial(4))

# Return remainder of division
print("fmod(5,4) = ", math.fmod(5, 4))

# Receive a float and return an int
print("trunc(4.2) = ", math.trunc(4.2))

# Return x^y
print("pow(2,2) = ", math.pow(2, 2))

# Return the square root
print("sqrt(4) = ", math.sqrt(4))

# Special values
print("math.e = ", math.e)
print("math.pi = ", math.pi)

# Return e^x
print("exp(4) = ", math.factorial(4))

# Return the natural logarithm e * e * e ~= 20 so log(20) tells
# you that e^3 ~= 20
print("log(20) = ", math.log(20))

# You can define the base and 10^3 = 1000
print("log(1000,10) = ", math.log(1000, 10))

# You can also use base 10 like this
print("log10(1000) = ", math.log10(1000))

# We have the following trig functions
# sin, cos, tan, asin, acos, atan, atan2, asinh, acosh,
# atanh, sinh, cosh, tanh

# Convert radians to degrees and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))

# ---------- ACCURATE FLOATING POINT CALCULATIONS ----------

# The decimal module provides for more accurate floating point calculations
# With from you can reference methods without the need to reference the module
# like we had to do with math above
# We create an alias being D here to avoid conflicts with methods with
# the same name
from decimal import Decimal as D

sum = D(0)
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum -= D("0.03")

print("Sum = ", sum)

# ---------- STRINGS ----------
# Text is stored using the string data type
# You can use type to see the data type of a value
print(type(3))
print(type(3.14))

# Single quotes or double are both used for strings
print(type("3"))
print(type('3'))

samp_string = "This is a very important string"

# Each character is stored in a series of boxes labeled with index numbers
# You can get a character by referencing an index
print(samp_string[0])

# Get the last character
print(samp_string[-1])

# Get the last character
print(samp_string[3 + 5])

# Get the string length
print("Length :", len(samp_string))

# Get a slice by saying where to start and end
# The 4th index isn't returned
print(samp_string[0:4])

# Get everything starting at an index
print(samp_string[8:])

# Join or concatenate strings with +
print("Green " + "Eggs")

# Repeat strings with *
print("Hello " * 5)

# Convert an int into a string
num_string = str(4)

# Cycle through each character with for
for char in samp_string:
    print(char)

# Cycle through characters in pairs
# Subtract 1 from the length because length is 1 more then the highest index
# because strings are 0 indexed
# Use range starting at index 0 through string length and increment by
# 2 each time through
for i in range(0, len(samp_string) - 1, 2):
    print(samp_string[i] + samp_string[i + 1])

# Computers assign characters with a number known as a Unicode
# A-Z have the numbers 65-90 and a-z 97-122

# You can get the Unicode code with ord()
print("A =", ord("A"))

# You can convert from Unicode with chr
print("65 =", chr(65))

# ---------- PROBLEM : SECRET STRING ----------
# Receive a uppercase string and then hide its meaning by turning
# it into a string of unicodes
# Then translate it from unicode back into its original meaning

norm_string = input("Enter a string to hide in uppercase: ")

secret_string = ""

# Cycle through each character in the string
for char in norm_string:

    # Store each character code in a new string
    secret_string += str(ord(char))

print("Secret Message :", secret_string)

norm_string = ""

# Cycle through each character code 2 at a time by incrementing by
# 2 each time through since unicodes go from 65 to 90
for i in range(0, len(secret_string) - 1, 2):

    # Get the 1st and 2nd for the 2 digit number
    char_code = secret_string[i] + secret_string[i + 1]

    # Convert the codes into characters and add them to the new string
    norm_string += chr(int(char_code))

print("Original Message :", norm_string)

# ---------- SUPER AWESOME MIND SCRAMBLING PROBLEM ----------
# Make the above work with upper and lowercase with 1 addition and
# 1 subtraction

# Add these 2 changes

# secret_string += str(ord(char) - 23)

# norm_string += chr(int(char_code) + 23)