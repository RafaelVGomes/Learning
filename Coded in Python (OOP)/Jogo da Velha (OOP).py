#!/usr/bin/python3
from os import system, name
cls = lambda: system('cls' if name=='nt' else 'clear')

ArrayCasas = [
            [1, 2, 3],
            [4, "X", 6],
            [7, 8, 9]
            ]
CasasVazias = []
class JogoDaVelha:
    def __init__(self, casa):
        self.casa = casa
            
    def Grade(self):
        cls()
        print('+---+---+---+')
        print('|', self.casa[0][0] ,'|', self.casa[0][1] ,'|', self.casa[0][2] ,'|')
        print('+---+---+---+')
        print('|', self.casa[1][0] ,'|', self.casa[1][1] ,'|', self.casa[1][2] ,'|')
        print('+---+---+---+')
        print('|', self.casa[2][0] ,'|', self.casa[2][1] ,'|', self.casa[2][2] ,'|')
        print('+---+---+---+')

    def CasasLivres(self):
        casas = self.casa
        for i in range(0, len(casas)):
            for j in casas[i]:
                if j != "X" and j != "O":
                    CasasVazias.append(j)
        
    def Jogador(self):
        Jogo.Grade()
        Jogo.CasasLivres()
        e = False
        while e == False:
            try:
                print('Escolha uma casa ou digite "0" para sair:' )
                escolha = int(input())
                if escolha == 0:
                    e = True

                elif escolha < 0 or escolha > 9:
                    Jogo.Grade()
                    print("Número inválido. Tente de 1 a 9.")
                    
                elif escolha not in CasasVazias:
                    Jogo.Grade()
                    print("Casa ocupada. Tente outra.")
                    print("Casas livres:", CasasVazias)
                
                else:
                    e = True

            except ValueError:
                Jogo.Grade()
                print("Entrada inválida. Use apenas números.")
                e = False
        
Jogo = JogoDaVelha(ArrayCasas)

Jogo.Jogador()

