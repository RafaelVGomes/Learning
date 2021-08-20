#!/usr/bin/python3
from os import system, name
cls = lambda: system('cls' if name=='nt' else 'clear')

class JogoDaVelha:
    
    def __init__(self, lista):
        self.lista = lista
        print("+---+---+---+")
        print("|", lista[0][0], "|", lista[0][1], "|", lista[0][2], "|")
        print("+---+---+---+")
        print("|", lista[1][0], "|", lista[1][1], "|", lista[1][2], "|")
        print("+---+---+---+")
        print("|", lista[2][0], "|", lista[2][1], "|", lista[2][2], "|")
        print("+---+---+---+")

    def CasasLivres(self):
        pass
    
    def Jogador(self):
        pass

    def Computador(self):
        pass
    
    def Atualizar(self):
        pass
        
    def FimDeJogo():
        pass

casas = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
n1 = 1
n2 = 1
# casas[n1][n2] = "X"

JogoDaVelha(casas)
