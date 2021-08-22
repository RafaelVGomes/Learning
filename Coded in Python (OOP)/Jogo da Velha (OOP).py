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

    vazio = []
    
    def __init__(self, casa):
        self.casa = casa
            
    def Grade(self):
        casa = self.casa
        cls()
        print('+---+---+---+')
        print('|', casa[0][0] ,'|', casa[0][1] ,'|', casa[0][2] ,'|')
        print('+---+---+---+')
        print('|', casa[1][0] ,'|', casa[1][1] ,'|', casa[1][2] ,'|')
        print('+---+---+---+')
        print('|', casa[2][0] ,'|', casa[2][1] ,'|', casa[2][2] ,'|')
        print('+---+---+---+')
        self.vazio = []
        Jogo.CasasLivres()
        
    def CasasLivres(self):
        casas = self.casa
        v = self.vazio
        for i in range(0, len(casas)):
            for j in range(0, len(casas[i])):
                if casas[i][j] != "X" and casas[i][j] != "O":
                    v.append(casas[i][j])
        
    def Jogador(self):
        Jogo.Grade()
        casa = self.casa
        e = False
        
        while e == False:
            try:
                escolha = int(input('Escolha uma casa ou digite "0" para sair: '))
                if escolha == 0:
                    e = True

                elif escolha < 0 or escolha > 9:
                    Jogo.Grade()
                    print("Número inválido. Tente de 1 a 9.")
                    
                elif escolha not in self.vazio:
                    Jogo.Grade()
                    print("Casa ocupada. Tente outra.")
                    print("Casas livres:", self.vazio)
                
                else:
                    for x in range(0, len(casa)):
                        for y in range(len(casa[x])):
                            if escolha == casa[x][y]:
                                casa[x][y] = "O"
                                e = True           
            except ValueError:
                Jogo.Grade()
                print("Entrada inválida. Use apenas números.")
                e = False
        
        Jogo.Computador()
        
    def Computador(self):
        casa = self.casa
        comp_escolha = choice(self.vazio)
        for x in range(0, len(casa)):
            for y in range(len(casa[x])):
                if comp_escolha == casa[x][y]:
                    casa[x][y] = "X"
                    Jogo.Jogador()
        
   

Jogo = JogoDaVelha(ArrayCasas)

Jogo.Jogador()

