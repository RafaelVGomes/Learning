#!/usr/bin/python3
import numpy as np
from os import system, name
cls = lambda: system('cls' if name=='nt' else 'clear')

class JogoDaVelha:
    def __init__(self, lista):
        self.lista = lista
        
    def Tabuleiro(self):
        print('+---+---+---+')
        print('|', self.lista[0][0] ,'|', self.lista[0][1] ,'|', self.lista[0][2] ,'|')
        print('+---+---+---+')
        print('|', self.lista[1][0] ,'|', self.lista[1][1] ,'|', self.lista[1][2] ,'|')
        print('+---+---+---+')
        print('|', self.lista[2][0] ,'|', self.lista[2][1] ,'|', self.lista[2][2] ,'|')
        print('+---+---+---+')
        pass

    def CasasLivres(self):
        if self.lista != "X" and self.lista != "O":
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
casasvazias = []
# n1 = 1
# n2 = 1
# casas[n1][n2] = "X"

cls()
obj = JogoDaVelha(casas)

print(obj.Tabuleiro())
