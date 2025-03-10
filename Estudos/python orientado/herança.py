# -*- coding: utf-8 -*-
"""
@author: joaobcamargos
:)
"""

class Animal:
    
    
    def __init__(self,especie):
        self.especie=especie
        
    def fazer_som(self): 
        print("o seu animal faz som")
    
class Cachorro(Animal):
        
        def __init__(self,especie,raca):
            super().__init__(especie)
            self.raca=raca
            
            self.raca=raca
            super().fazer_som()
        def fazer_som(self):
            super.fazer_som()
            print("o Seu cachorro",self.especie,"da raça",self.raça,"au au")
        

MeuCachorro=Cachorro()
            