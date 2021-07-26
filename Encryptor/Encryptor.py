from os import system
system('cls')
#This program shold encrypt sentences using a key between 1 and 25.
#Using default values for now. 

inp = input("Digite texto para codificar: ")
inp = list(inp)

#This is the Shift Value. It'll say how many letters we'll be displaced.
svStatus = False
while svStatus == False:
    try:
        sv = int(input("Número codificador (1 ~ 24): "))

        if sv < 1 or sv > 24:
            print("Número inválido.")
            svStatus = False
        
        else:
            svStatus = True

    except ValueError:
        print("Entrada inválida. Use apenas números.")
        svStatus = False


#Encrypted sentence at the end.
cipher = ''

for char in inp:
    if not char.isalpha():
        cipher += char
        continue
    
    if char == 'Z':
        char2 = 65 + (sv - 1)
        cipher += chr(char2)
        char2 = chr(char2)
    
    elif char == 'z':
        char3 = 97 + (sv - 1)
        cipher += chr(char3)
        char3 = chr(char3)
    
    else:
        char4 = ord(char) + sv
        cipher += chr(char4)
    
print()
print("Criptografado:", cipher)
print()