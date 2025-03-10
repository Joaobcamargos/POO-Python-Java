# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:39:13 2024

@author: joaobcamargos
"""

class Carro:
    def __init__(self,modelo,ano,cor,vel,vmax):
        self.modelo=modelo
        self.ano=ano
        self.cor=cor
        self.vel=vel
        self.vmax=vmax
    
    def pare(self):
        self.vel=0
        print('parei o carro')
        
    def acelere(self,vel):
        if(vel>self.vel):
            self.vel=vel
            print("acelerei para",vel,self.vmax)
        else:
            print('velocidade esquisita')
        

def main():
    carro1=Carro('uno','1988','vermelho',4,160)
    carro1.pare()
    carro1.acelere(180)
    
    
main()