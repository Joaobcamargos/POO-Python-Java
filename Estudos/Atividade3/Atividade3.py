# -*- coding: utf-8 -*-
"""
@author: joaobcamargos
:)
"""

class Cliente:
    def __init__(self,nome,dias_estadia,consumo_restaurante):
        self.nome=nome
        self.dias_estadia=dias_estadia
        self.consumo_restaurante=consumo_restaurante #Dita quantas refeições foram consumidas , ex:2 refeições
        
    def fornecerValorConta(self):
        valordiaria=self.dias_estadia*100
        valorrestaurante=self.consumo_restaurante*50
        valortot=valordiaria+valorrestaurante
        return valortot
    
class Hotel:
    def __init__(self,nome_hotel):
        self.nome_hotel=nome_hotel
        
    def determineContaCliente(self,Cliente):
        a=Cliente.fornecerValorConta()
        print("O cliente",Cliente.nome,"Ficou hospedado por",Cliente.dias_estadia,"dias","comeu",Cliente.consumo_restaurante,"refeições","e sua conta final foi:",a)


def Main():
    Hotel1=Hotel("RsHoteis")
    Cliente1=Cliente('RogerioDosSantos',3,4)
    Cliente1.fornecerValorConta()
    Hotel1.determineContaCliente(Cliente1)
Main()
        
#Resultado:Nesse código foi implementado um código no qual tinha como objetivo entender a troca de mensagens entre objetos.
#O código em questão foi bem sucedido , é feito uma troca de mensagens entre o hotel e o cliente a partir do método determineContaCliente
#que chama outro método da classe Cliente a partir de um parâmetro de objeto.
        
        
        