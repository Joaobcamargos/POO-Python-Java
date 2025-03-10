# -*- coding: utf-8 -*-
"""
@author: joaobcamargos
:)
"""

class Perceptron:
    def __init__(self)->None:
        self.pesos=[]
        self.entradas=[]
    def receberentradas(self)->None:
        print('Digite quantas entradas vai querer')
        n=int(input())
        for i in range(n):
            print('Digite a entrada',i+1)
            self.entradas.append(int(input()))
    
    def setarpesos(self)->None:
        if len(self.entradas)==0:
            print('Adicione as entradas primeiro')
        else:
            for i in range(len(self.entradas)):
                print('Digite o peso para entrada',self.entradas[i])
                self.pesos.append(int(input()))
            
    def funcaosoma(self)->float:
        soma = 0
        if(len(self.entradas)!=0):
            for i in range(len(self.entradas)):
              soma += self.entradas[i]*self.pesos[i]
        else:
            print("error!")
        return soma
    
    def funcativacao(self)->bool:
        somaR = self.funcaosoma()
        if somaR > 0:
            return True
        else:
            return False

def main():
    p = Perceptron()
    p.receberentradas()
    p.setarpesos()
    
    soma = p.funcaosoma()
    print("Soma: ", soma)


    ativacao = p.funcativacao()
    print("Ativação: ", ativacao)

if __name__ == "__main__":
    main()
       