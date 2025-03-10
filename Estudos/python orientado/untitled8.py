# -*- coding: utf-8 -*-
"""
@author: joaobcamargos
:)
"""

class FazBolo:
    
    def __int__(self,massa,recheio,cobertura,temponoforno,fogo):
        self.massa=massa
        self.recheio=recheio
        self.cobertura=cobertura
        
        def Assar(self,tempo,fogo):
            print('Você está querendo assar o bolo no fogo',fogo,'por',tempo,'minutos')
            if fogo == 'alto':
                if tempo < 10:
                    print('Tempo insuficiente')
                elif tempo >10:
                    print('Tempo excedido')
                    
            elif fogo =='medio':
                if tempo<30:
                    print('Tempo insuficiente')
                elif tempo>30:
                    print('Tempo excedido')
            elif fogo =='baixo':
                if tempo <45:
                    print('Tempo suficiente')
                elif tempo>45:
                    print('Tempo excedido')
            else:
                print('parametros indevidos')
            
def Main():
    Bolo1=FazBolo('Fermentada','Baunilha','Chocolate')
    Bolo1.assar(15,'alto')
                
Main()