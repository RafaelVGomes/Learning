#!/usr/bin/python3
import numpy as np
from os import system, name
cls = lambda: system('cls' if name=='nt' else 'clear')

ArrayCasas = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
CasasVazias = []
class JogoDaVelha:
    def __init__(self, casa):
        self.casa = casa
        print('+---+---+---+')
        print('|', self.casa[0][0] ,'|', self.casa[0][1] ,'|', self.casa[0][2] ,'|')
        print('+---+---+---+')
        print('|', self.casa[1][0] ,'|', self.casa[1][1] ,'|', self.casa[1][2] ,'|')
        print('+---+---+---+')
        print('|', self.casa[2][0] ,'|', self.casa[2][1] ,'|', self.casa[2][2] ,'|')
        print('+---+---+---+')
  
    def CasasLivres(self):
        if self.casa != "X" and self.casa != "O":
            pass
    
    def Jogador(self):
        pass

    def Computador(self):
        pass
    
    def Atualizar(self):
        pass
        
    def FimDeJogo():
        pass

cls()
obj = JogoDaVelha(ArrayCasas)

print(obj())
