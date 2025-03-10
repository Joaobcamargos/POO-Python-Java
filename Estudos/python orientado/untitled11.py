# -*- coding: utf-8 -*-
"""
@author: joaobcamargos
:)
"""

from abc import ABC, abstractmethod

class Usuario(ABC):
    usuarios = []

    def __init__(self, nome, senha, email):
        self.nome = nome
        self.senha = senha
        self.email = email

    def salvar_banco_Dados(self, arquivo):
        with open(arquivo, 'w') as f:
            for usuario in self.usuarios:
                f.write(f"{usuario.nome},{usuario.email}\n")

    @abstractmethod 
    def cadastrar(self, a, b, c):
        pass

class Funcionario(Usuario):
    def __init__(self, cargo, nome, senha, email):
        super().__init__(nome, senha, email)
        self.cargo = cargo

    def cadastrar(self, nome, senha, email):
        if any(usuario.nome == nome for usuario in Usuario.usuarios):
            print('Nome de usuário já cadastrado ERROR!')
        else:
            Usuario.usuarios.append(Funcionario(self.cargo, nome, senha, email))

class Cliente(Usuario):
    def __init__(self, nivel, nome, senha, email):
        super().__init__(nome, senha, email)
        self.nivel = nivel

    def cadastrar(self, nome, senha, email):
        if any(usuario.nome == nome for usuario in Usuario.usuarios):
            print('Nome de usuário já cadastrado ERROR!')
        else:
            Usuario.usuarios.append(Cliente(self.nivel, nome, senha, email)) #self é quando é da propria classe mas naquele caso era da super

# Exemplo de uso
funcionario = Funcionario("Desenvolvedor", "funcionario1", "senha123", "funcionario1@email.com")
funcionario.cadastrar("funcionario2", "outrasenha", "funcionario2@email.com")

cliente = Cliente("premium", "cliente1", "senha123", "cliente1@email.com")
cliente.cadastrar("cliente2", "outrasenha", "cliente2@email.com")

# Salvando os dados em um arquivo
funcionario.salvar_banco_Dados("usuarios.txt")
cliente.salvar_banco_Dados("usuarios.txt")
