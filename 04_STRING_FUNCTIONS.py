# ---------- STRING METHODS ----------

# Strings have many methods we can use beyond what I covered last time
rand_string = "   this is an important string   "

# Delete whitespace on left
rand_string = rand_string.lstrip()

# Delete whitespace on right
rand_string = rand_string.rstrip()

# Delete whitespace on right and left
rand_string = rand_string.strip()

# Capitalize the 1st letter
print(rand_string.capitalize())

# Capitalize every letter
print(rand_string.upper())

# lowercase all letters
print(rand_string.lower())

# Turn a list into a string and separate items with the defined
# separator
a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

# Convert a string into a list
a_list_2 = rand_string.split()

for i in a_list_2:
    print(i)

# Count how many times a string occurs in a string
print("How many is :", rand_string.count("is"))

# Get index of matching string
print("Where is string :", rand_string.find("string"))

# Replace a substring
print(rand_string.replace("an ", "a kind of "))

# ---------- PROBLEM : ACRONYM GENERATOR ----------
# You will enter a string and then convert it to an acronym
# with uppercase letters like this
'''
Convert to Acronym : Random Access Memory
RAM
'''

# Ask for a string
orig_string = input("Convert to Acronym : ")

# Convert the string to all uppercase
orig_string = orig_string.upper()

# Convert the string into a list
list_of_words = orig_string.split()

# Cycle through the list
for word in list_of_words:

    # Get the 1st letter of the word and eliminate the newline
    print(word[0], end="")

print()

# ---------- MORE STRING METHODS ----------
# For our next problem some additional string methods are going to be
# very useful

letter_z = "z"
num_3 = "3"
a_space = " "

# Returns True if characters are letters or numbers
# Whitespace is false
print("Is z a letter or number :", letter_z.isalnum())

# Returns True if characters are letters
print("Is z a letter :", letter_z.isalpha())

# Returns True if characters are numbers (Floats are False)
print("Is 3 a number :", num_3.isdigit())

# Returns True if all are lowercase
print("Is z a lowercase :", letter_z.islower())

# Returns True if all are uppercase
print("Is z a uppercase :", letter_z.isupper())

# Returns True if all are spaces
print("Is space a space :", a_space.isspace())


# ---------- MAKE A isfloat FUNCTION ----------
# There is no way to check if a string contains a float
# so let's make one by defining our own function

# Functions allow use to avoid repeating code
# They can receive values (attributes / parameters)
# They can return values

# You define your function name and the names for the values
# it receives like this

def isfloat(str_val):
    try:

        # If the string isn't a float float() will throw a
        # ValueError
        float(str_val)

        # If there is a value you want to return use return
        return True
    except ValueError:
        return False


pi = 3.14

# We call our functions by name and pass in a value between
# the parentheses
print("Is Pi a Float :", isfloat(pi))

# ---------- PROBLEM : CAESAR'S CIPHER ----------
# Receive a message and then encrypt it by shifting the
# characters by a requested amount to the right
# A becomes D, B becomes E for example
# Also decrypt the message back again

# A-Z have the numbers 65-90 in unicode
# a-z have the numbers 97-122
# You get the unicode of a character with ord(yourLetter)
# You convert from unicode to character with chr(yourNumber)

# You should check if a character is a letter and if not
# leave it as its default

# Hints
# Use isupper() to decided which unicodes to work with
# Add the key (number of characters to shift) and if
# bigger or smaller then the unicode for A, Z, a, or z
# increase or decrease by 26

# Receive the message to encrypt and the number of characters to shift
message = input("Enter your message : ")
key = int(input("How many characters should we shift (1 - 26)"))

# Prepare your secret message
secret_message = ""

# Cycle through each character in the message
for char in message:

    # If it isn't a letter then keep it as it is in the else below
    if char.isalpha():

        # Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key

        # If uppercase then compare to uppercase unicodes
        if char.isupper():

            # If bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26

            # If smaller than A add 26
            elif char_code < ord('A'):
                char_code += 26

        # Do the same for lowercase characters
        else:
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26

        # Convert from code to letter and add to message
        secret_message += chr(char_code)

    # If not a letter leave the character as is
    else:
        secret_message += char

print("Encrypted :", secret_message)

# To decrypt the only thing that changes is the sign of the key
key = -key

orig_message = ""

for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            elif char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26

        orig_message += chr(char_code)

    else:
        orig_message += char

print("Decrypted :", orig_message)

# ---------- EXTRA HOMEWORK ----------
# For homework put the duplicate code above in a function