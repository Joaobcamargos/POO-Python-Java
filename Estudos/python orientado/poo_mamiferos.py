# -*- coding: utf-8 -*-
"""
@author: joaobcamargos
:)
"""

class Mamiferos:
    
    def __init__(self,nome):
        self.nome=nome
        
    def comer(self):
        print("O seu mamifero está comendo")
        
    def sentar(self):
        print("O seu mamifero está sentado")
    
    def dormir(self):
        print("o seu animmal está dormindo")
        
class Caes(Mamiferos):
    
    def __init__(self,nome,raca):
        super().__init__(nome)
        self.raca=raca
        
    def PegaBola(self):
        print("O seu cão está pegando a bola")

class Gato(Mamiferos,pelagem):
    
    def __init__(self,nome,pelagem):
        super().__init__(nome)
        self.pelagem=pelagem
        
        
    def Brincar(self):
        print("O gato esta brincando")

class Equinos(Mamiferos):
    def __init__(self,nome,porte):
        super().__init__(nome)
        self.porte=porte
    def
    
class Roedores(Mamiferos)
        
        
        