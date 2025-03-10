# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:56:15 2024

@author: joaobcamargos
"""

class Bolo:
    Nome=""
    Recheio=""
    Massa=""
    tem_cobertura=True
#instânciar->
bolo1=Bolo()
bolo2=Bolo()
bolo3=Bolo()

bolo1.tem_cobertura=False
bolo3.tem_cobertura=True

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
