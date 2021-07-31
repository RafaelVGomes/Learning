from os import system
system('cls')

# Comparing words
def WordsCheck():
    st = False
    while st == False:   
        # User's input
        UserInput1 = input("Digite uma palavra: ").lower()
        UserInput2 = input("Digite outra palavra: ").lower()
        if UserInput1 == "0" or UserInput2 == 0:
            exit()
        elif UserInput1 == UserInput2:
            st == False
            print("\n", "Use palavras diferentes. Digite 0 para sair.", "\n")
        else:
            AnagramCheck(UserInput1, UserInput2)

# Comparing words letters
def AnagramCheck(word1, word2):
    if word1 != word2:
        word1.sort()
        word2.sort()
    elif word1 == word2:
        print("\n", "Is a anagram.", "\n")
    else:
        print("\n", "Is not a anagram.", "\n")

WordsCheck()