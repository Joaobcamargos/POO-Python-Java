# -*- coding: utf-8 -*-
"""
@author: joaobcamargos
:)
"""

class FazBolo:
    def __init__(self, massa, recheio, cobertura):
        self.massa = massa
        self.recheio = recheio
        self.cobertura = cobertura

    def Assar(self, tempo, fogo):
        self.tempo=tempo
        self.fogo=fogo
        print(f'Você está querendo assar o bolo no fogo {fogo} por {tempo} minutos')
        if self.fogo == 'alto':
            if self.tempo < 10:
                print('Tempo insuficiente')
            elif self.tempo > 10:
                print('Tempo excedido')
        elif self.fogo == 'medio':
            if self.tempo < 30:
                print('Tempo insuficiente')
            elif self.tempo > 30:
                print('Tempo excedido')
        elif self.fogo == 'baixo':
            if self.tempo < 45:
                print('Tempo suficiente')
            elif self.tempo > 45:
                print('Tempo excedido')

        else:
            print('Parâmetros inválidos')


            
def Main():
    bolo_de_chocolate = FazBolo('Fermentada', 'Chocolate', 'Chantilly') 
    bolo_de_chocolate.Assar(10, 'medio') 
    bolo_de_chocolate.Assar(10000, 'medio') 
    bolo_de_chocolate.Assar(0, 'o')
Main()

# Resultados: Neste código,foi implementado e testado o construtor def __init__ e o metodo def Assar , além disso também 
# foi utilizado um tratamento de erros básico.