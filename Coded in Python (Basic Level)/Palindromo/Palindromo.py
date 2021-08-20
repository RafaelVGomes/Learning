#/usr/bin/python3
from os import system
system('cls')

# User's input
UserInput = input("Enter a word: ")
UserInput = UserInput.lower()
reverse = []

# Reversing user's input
for i in UserInput:
    reverse.insert(0, i)

# Formating reversed input
reverse = ''.join(reverse)
reverse = reverse.lower()

# Checks if UserInput and reverse are the same word
print()
if reverse == UserInput:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
print()