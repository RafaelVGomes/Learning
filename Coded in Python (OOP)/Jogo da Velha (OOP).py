#!/usr/bin/python3
from random import choice
from os import system, name
cls = lambda: system('cls' if name=='nt' else 'clear')

ArrayCasas = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]

class JogoDaVelha:
    
    def __init__(self, casa, nível):
        self.casa = casa
        self.nível = nível
            
    def Grade(self):
        casa = self.casa
        cls()
        print("Nível:", self.nível)
        print('+---+---+---+')
        print('|', casa[0][0] ,'|', casa[0][1] ,'|', casa[0][2] ,'|')
        print('+---+---+---+')
        print('|', casa[1][0] ,'|', casa[1][1] ,'|', casa[1][2] ,'|')
        print('+---+---+---+')
        print('|', casa[2][0] ,'|', casa[2][1] ,'|', casa[2][2] ,'|')
        print('+---+---+---+')
        Jogo.CasasLivres()
        
    def CasasLivres(self):
        vazias = []
        casas = self.casa
        
        for i in range(0, len(casas)):
            for j in range(0, len(casas[i])):
                if casas[i][j] != "X" and casas[i][j] != "O":
                    vazias.append(casas[i][j])
        
        return vazias

    def Jogador(self):
        Jogo.Grade()
        casa = self.casa
        e = False
        
        while e == False:
            try:
                escolha = int(input('Escolha uma casa ou digite "0" para sair: '))
                if escolha == 0:
                    print("Corre, seu frouxo!!!")
                    exit(0)

                elif escolha < 0 or escolha > 9:
                    Jogo.Grade()
                    print("Número inválido. Tente de 1 a 9.")
                    
                elif escolha not in Jogo.CasasLivres():
                    Jogo.Grade()
                    print("Casa ocupada. Tente outra.")
                    print("Casas livres: ", Jogo.CasasLivres())
                    
                else:
                    for x in range(0, len(casa)):
                        for y in range(len(casa[x])):
                            if escolha == casa[x][y]:
                                casa[x][y] = "O"
                                e = True           
            
            except ValueError:
                Jogo.Grade()
                print("Entrada inválida. Use apenas números.")
                
        Jogo.Resultado()
        Jogo.Computador()
        
    def Computador(self):
        casa = self.casa
        if len(Jogo.CasasLivres()) > 0:
            comp_escolha = choice(Jogo.CasasLivres())
            for x in range(0, len(casa)):
                for y in range(len(casa[x])):
                    if comp_escolha == casa[x][y]:
                        casa[x][y] = "X"
                        Jogo.Resultado()
                        Jogo.Jogador()
        else:
            pass

    def Resultado(self):
        casas = self.casa
        temp = []
        
        # Checando empate
        if len(Jogo.CasasLivres()) == 0:
            return Jogo.FimDeJogo("EMPATE!")

        # Checando linhas
        for i in range(0, 3):
            temp = []
            for j in range(0,3):
                temp.append(casas[i][j])
                if temp == ["X", "X", "X"]:
                    return Jogo.FimDeJogo("Você perdeu")
                    
                if temp == ["O", "O", "O"]:
                    return Jogo.FimDeJogo("Você venceu!")
        
        # Checando colunas
        c1 = 0
        c2 = 1
        while c2 < 4:
            for i in range(0, 3):
                for j in range(c1, c2):
                    temp.append(casas[i][j])
                    if temp == ["X", "X", "X"]:
                        return Jogo.FimDeJogo("Você perdeu")
                        
                    if temp == ["O", "O", "O"]:
                        return Jogo.FimDeJogo("Você venceu!")
                        
            temp = []
            c1 += 1
            c2 += 1

        # Checando Diagonais
        casa = self.casa
        temp = []
        temp.append(casa[0][0])
        temp.append(casa[1][1])
        temp.append(casa[2][2])

        if temp == ["X", "X", "X"]:
            return Jogo.FimDeJogo("Você perdeu")
            
        if temp == ["O", "O", "O"]:
            return Jogo.FimDeJogo("Você venceu!")

        temp = []
        temp.append(casa[0][2])
        temp.append(casa[1][1])
        temp.append(casa[2][0])

        if temp == ["X", "X", "X"]:
            return Jogo.FimDeJogo("Você perdeu")
            
        if temp == ["O", "O", "O"]:
            return Jogo.FimDeJogo("Você venceu!")
                            
    def FimDeJogo(self, resultado):
            self.resultado = resultado
            Jogo.Grade()
            print(self.resultado)
            exit()

cls()
print("""Escolha o nível de dificuldade do tabuleiro:
1. Normal
2. Difícil
3. Que porra é essa, véi?!""")

e = False
while e == False:
    try:
        escolha = int(input('Ou digite "0" e vá pro colo da mamãe: '))
        if escolha == 0:
            print("Volta pra teta da tua mãe, neném!")
            exit(0)

        elif escolha < 0 or escolha > 3:
            print("É doido ou se faz?! De 1 a 3, mané!")

        else:
            D = {1: "Normal", 2: "Difícil", 3: "Que porra é essa, véi?!"}
            if escolha == 1:
                Jogo = JogoDaVelha(ArrayCasas, D[escolha])
                Jogo.Jogador()

            if escolha == 2:
                ArrayCasas[1][1] = "X"
                Jogo = JogoDaVelha(ArrayCasas, D[escolha])
                Jogo.Jogador()

            if escolha == 3:
                ArrayCasas[0][0] = "X"
                ArrayCasas[0][2] = "X"
                ArrayCasas[2][0] = "X"
                ArrayCasas[2][2] = "X"
                Jogo = JogoDaVelha(ArrayCasas, D[escolha])
                Jogo.Jogador()
    
    except ValueError:
                print("Tá me zuando?! Use números, zé ruela!")

Jogo = JogoDaVelha(ArrayCasas)
Jogo.Jogador()

