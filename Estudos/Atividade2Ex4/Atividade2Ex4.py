# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:56:15 2024

@author: joaobcamargos
"""

class Bolo:
    def __init__(self,nome,recheio,massa,tem_cobertura):
        self.nome=nome
        self.recheio=recheio
        self.massa=massa
        self.tem_cobertura= tem_cobertura #Se colocar True vai ser sempre true , independende do que você instânciar.
    
#instânciar->
bolo1=Bolo('Chocolate','brigadeiro','fermentada',True)
bolo2=Bolo('Iogurte','Creme','fofa',False)
bolo3=Bolo('Chocolate','chocolate','fermentada',False)

print(bolo3.tem_cobertura)
print(bolo1.tem_cobertura)

bolo1=bolo3
bolo3.tem_cobertura=False 

print(bolo3.tem_cobertura)
print(bolo1.tem_cobertura)

# Resultados: Neste código, observamos a diferença entre instanciar objetos separadamente da classe principal
# e instanciar um objeto a partir de outro. Essa diferença está relacionada aos ponteiros em Python.
#Ao instanciarmos um objeto a partir de outro, estamos criando um ponteiro de um objeto que aponta para o outro.
#Portanto, se mudarmos uma característica de um objeto, essa característica será alterada no outro objeto também.
#Além disso também testamos o construtor a partir da função __init__().
