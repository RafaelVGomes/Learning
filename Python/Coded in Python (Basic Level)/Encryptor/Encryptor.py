from os import system
system('cls')
#This program should encrypt (and now also decrypt) sentences using a key between -24 and 24, except 0.
#And can't change numbers and any other char. (Challenge asked for this.)
#Mixing portuguese and english language on porpose.

inp = input("Digite texto para codificar: ")
inp = list(inp)

#This is the Shift Value. It'll say how many houses letters will be displaced.
svStatus = False
while svStatus == False:
    try:
        sv = int(input('''
    Número codificador (1 ~ 24)
    ou decodificador (-24 ~ -1): '''))

        if sv > 24 or sv < -24:
            print("    Número inválido.")
            svStatus = False
        
        elif sv == 0:
            print("    Número inválido.")
            svStatus = False

        else:
            svStatus = True

    except ValueError:
        print("    Entrada inválida. Use apenas números.")
        svStatus = False

#Encrypted sentence at the end.
cipher = ''

if sv > 0:
#Encrypt
    for char in inp:
        if not char.isalpha():
            cipher += char
            #print("C0:", char, ord(char))
            continue
        
        code = ord(char) + sv
        
        if code > 90 and code < 97:
            code3 = (code - 91) + 65
            #print("C2:", chr(code3), code3)
            cipher += chr(code3)
        elif code > 122:
            code2 = (code - 123) + 97
            #print("C2:", chr(code2), code2)
            cipher += chr(code2)
        else:
            #print("C1:", chr(code), code)
            cipher += chr(code)
    print()
    print("Criptografado:", cipher)
    print()

#Decrypt
else:
    for char in inp:
        if not char.isalpha():
            cipher += char
            #print("-C0:", char, ord(char))
            continue
        
        code = ord(char) + sv
        
        if code < 65:
            code3 = (code + 91) - 65
            #print("-C2:", chr(code3), code3)
            cipher += chr(code3)

        elif code < 97 and code > 90:
            code2 = (code + 123) - 97
            #print("-C2:", chr(code2), code2)
            cipher += chr(code2)

        else:
            #print("-C1:", chr(code), code)
            cipher += chr(code)
    print()
    print("Decriptografado:", cipher)
            
print()