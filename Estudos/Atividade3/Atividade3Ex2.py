# -*- coding: utf-8 -*-
"""
@author: joaobcamargos
:)
"""

class Carro:
    def __init__(self,modelo,cor,ligado,velocidade):
        self.modelo=modelo
        self.cor=cor
        self.ligado=ligado
        self.velocidade=velocidade
    def acelerar(self,vel):
        if type(vel)==float or type(vel) == int:
            if vel<self.velocidade:
             self.velocidade=vel
            else:
                print("Não é possivel acelerar para essa velocidade , visto que você já está em uma velocidade maior que a pretendida")
        else:
            print("parâmetro invalido")
        print("o carro do modelo:",self.modelo,"acelerou para",vel)
    def ligar(self):
        self.ligado=True
        print("O carro do modelo:",self.modelo,"esta ligado")
    def desligar(self):
        self.ligado=False
        print("O carro do modelo:",self.modelo,"esta desligado")
        
class Motorista:
    def __init__(self,nome):
        self.nome=nome
    def dirigir(self,Carro,velo):
        Carro.ligar()
        if type(velo)==float or type(velo) == int:
            Carro.acelerar(velo)
        else:
            print("parametro invalido")

def Main():
    Carro1=Carro('fusca','preto',True,10)
    Motorista1=Motorista('joao')
    Motorista1.dirigir(Carro1,11)
    Carro2=Carro('civic','cinza',False,0)
    Motorista2=Motorista('Maria Eduarda')
    Motorista2.dirigir(Carro2,"bleh")
    

Main()

#Resultados: Neste código foi feito novamente a interação entre objetos , nesse caso de forma mais elaborada, além disso foi feito
#alguns tratamentos de exceções que podem ser vistos nos exemplos na Main().