from os import system
system('cls')

# User's input
UserInput1 = list(input("Digite: ").lower())
UserInput2 = list(input("Digite: ").lower())

# Comparing words letters
def AnagramCheck(word1, word2):
    ReverseWord = []
    for i in word2:
        ReverseWord.insert(0, i)
    
    if word1 == ReverseWord:
        print("\n", "Is a anagram.", "\n")
    else:
        print("\n", "Is not a anagram.", "\n")

AnagramCheck(UserInput1, UserInput2)
