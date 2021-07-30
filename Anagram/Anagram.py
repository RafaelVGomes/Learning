from os import system
system('cls')

# User's input
UserInput1 = "Listen".lower()
UserInput2 = "Silent".lower()

# Comparing words letters
def AnagramCheck(word1, word2):
    if word1 in word2:
        print("\n", "Is a anagram.", "\n")
    else:
        print("\n", "Is not a anagram.", "\n")

AnagramCheck(UserInput1, UserInput2)