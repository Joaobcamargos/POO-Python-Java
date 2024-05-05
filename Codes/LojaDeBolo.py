# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:07:16 2024

@author: maece
"""

class Bolo:
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data
    
    def DefRecheio(self):
        pass
    
    def DefPeso(self):
        pass
    
    def DefCobertura(self):
        pass
    
    def DefPreco(self):
        pass


class BoloChocolate(Bolo):
    def __init__(self, nome, data):
        super().__init__(nome, data)
        self.recheio = None
        self.peso = None
        self.cobertura = None

    def DefRecheio(self):
        print('Opções de recheio: - Digite 1 para recheio de menta verde - Digite 2 para geleia de abacaxi')
        recheado = int(input())
        if recheado == 1:
            self.recheio = 'Menta verde'
        elif recheado == 2:
            self.recheio = 'Geleia de abacaxi'
        else:
            print('Opção inválida')

    def DefPeso(self):
        print('Qual será o peso do seu bolo em gramas? (Observação: peso máximo é 1002 gramas)')
        pesim = int(input())
        while pesim > 1002:
            print('Peso excede o máximo permitido. Por favor, insira um novo peso:')
            pesim = int(input())
        self.peso = pesim
    
    def DefCobertura(self):
        print('Opções de cobertura: - Digite 1 para cobertura de café expresso - Digite 2 para cobertura de bombom')
        coberto = int(input())
        if coberto == 1:
            self.cobertura = 'Café expresso'
        elif coberto == 2:
            self.cobertura = 'Bombom'
        else:
            print('Opção inválida')

    def DefPreco(self):
        custo_recheio = 5  
        custo_cobertura = 3 
        custo_fixo = 10  
        margem_lucro = 0.5  
        
        custo_total = (custo_recheio + custo_cobertura) * self.peso + custo_fixo
        preco_justo = custo_total * (1 + margem_lucro)
        
        return preco_justo


class BoloBaunilha(Bolo):
    def __init__(self, nome, data):
        super().__init__(nome, data)
        self.recheio = None
        self.peso = None
        self.cobertura = None

    def DefRecheio(self):
        print('Opções de recheio: - Digite 1 para recheio de baunilha com morangos - Digite 2 para creme de baunilha')
        recheado = int(input())
        if recheado == 1:
            self.recheio = 'Baunilha com morangos'
        elif recheado == 2:
            self.recheio = 'Creme de baunilha'
        else:
            print('Opção inválida')

    def DefPeso(self):
        print('Qual será o peso do seu bolo em gramas? (Observação: peso máximo é 1002 gramas)')
        pesim = int(input())
        while pesim > 1002:
            print('Peso excede o máximo permitido. Por favor, insira um novo peso:')
            pesim = int(input())
        self.peso = pesim
    
    def DefCobertura(self):
        print('Opções de cobertura: - Digite 1 para cobertura de chantilly - Digite 2 para cobertura de coco ralado')
        coberto = int(input())
        if coberto == 1:
            self.cobertura = 'Chantilly'
        elif coberto == 2:
            self.cobertura = 'Coco ralado'
        else:
            print('Opção inválida')

    def DefPreco(self):
        custo_recheio = 4  
        custo_cobertura = 2
        custo_fixo = 8  
        margem_lucro = 0.5  
        
        custo_total = (custo_recheio + custo_cobertura) * self.peso + custo_fixo
        preco_justo = custo_total * (1 + margem_lucro)
        
        return preco_justo


def Main():
    print("Preço justo para o bolo de chocolate:")
    bolo_chocolate = BoloChocolate("Maria", "2024-05-06")
    bolo_chocolate.DefRecheio()
    bolo_chocolate.DefPeso()
    bolo_chocolate.DefCobertura()
    print(f"Preço justo: R${bolo_chocolate.DefPreco()}")

    print("\nPreço justo para o bolo de baunilha:")
    bolo_baunilha = BoloBaunilha("João", "2024-05-07")
    bolo_baunilha.DefRecheio()
    bolo_baunilha.DefPeso()
    bolo_baunilha.DefCobertura()
    (f"Preço justo: R${bolo_baunilha.DefPreco()}")
Main()