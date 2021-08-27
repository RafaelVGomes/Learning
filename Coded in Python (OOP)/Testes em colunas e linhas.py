ArrayCasas = [
            [1, 2, 3],
            [4, 5, 6],
            ["X", "X", "X"]
            ]

temp = []

# Teste com linhas
for i in range(0, 3):
    temp = []
    temp.append(ArrayCasas[i])
    print(temp)
    if temp == [["X", "X", "X"]]:
        print("Você perdeu")
        break

    if temp == ["O", "O", "O"]:
        print("Você venceu!")
        break


# Teste com colunas
c1 = 0
c2 = 1

# while c2 < 4:
#     for i in range(0, 3):
#         for j in range(c1, c2):
#             print("c1:", c1, "e", "c2:", c2)
#             print("2D Array"+'['+str(i)+']'+'['+str(j)+']'+":", ArrayCasas[i][j])
#             temp.append(ArrayCasas[i][j])
#             if len(temp) < 3:
#                 print()
#             else:
#                 print(temp)
#     print()
#     temp = []        
#     c1 += 1
#     c2 += 1

