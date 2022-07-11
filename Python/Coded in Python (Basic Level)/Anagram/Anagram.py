#/usr/bin/python3
from os import system
system('cls')

# Comparing words
def WordsCheck():
    global UserInput1
    global UserInput2
    st = False
    while st == False:   
        # First user's input and "0" to EXIT
        print("Digite 0 para sair.")
        UserInput1 = input("Digite uma palavra: ")
        if UserInput1 == "0":
            exit()
        
        # Second user's
        UserInput2 = input("Digite outra palavra: ")
        
        # Treating UserInput1 and 2 as lower case
        ui1 = UserInput1.lower()
        ui2 = UserInput2.lower()
        
        # Comparing Words. If different calls AnagramCheck()
        if ui1 == ui2:
            st == False
            system('cls')
            print("Use palavras diferentes.", "\n")
        else:
            AnagramCheck(ui1, ui2)

# Comparing words letters
def AnagramCheck(word1, word2):
    # Treating lower cases entries as lists and sorting them
    word1 = list(word1)
    word2 = list(word2)
    word1.sort()
    word2.sort()
    
    # If all letters matchs or not, print an answer
    if word1 == word2:
        system('cls')
        print("\n", UserInput1, "e", UserInput2, "são anagramas.", "\n")
    else:
        system('cls')
        print("\n", UserInput1, "e", UserInput2, "não são anagramas.", "\n")

WordsCheck()