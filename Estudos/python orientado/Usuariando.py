from typing import Type
from abc import ABC , abstractmethod

Usuarios = []

class UsuarioI(ABC):
    @abstractmethod
    def confirmar(self) -> int:
        pass
    
    @abstractmethod
    def getUsuario(self) -> str:
        pass
    
    @abstractmethod
    def getEmail(self) -> str:
        pass
    
class Usuario(UsuarioI):
    def __init__(self, email: str, usuario: str) -> None:
        self.email = email
        self.usuario = usuario
    
    def getUsuario(self) -> str:
        return self.usuario
    
    def getEmail(self) -> str:
        return self.email
    
    def confirmar(self) -> int:
        if self.usuario in Usuarios:
            print('Usuário cadastrado')
            return 0
        else:
            print('Usuário não cadastrado')
            return 1

class Cadastro:
    def Cadastrar_Usuario(self, objeto: Type[UsuarioI]) -> None:
        if objeto.confirmar() != 0:
            Usuarios.append(objeto.getUsuario())
            print('Cadastrando usuario')

def Main():
    # Criando um objeto de Cadastro
    cadastro = Cadastro()
    
    # Cadastrando um usuário
    usuario1 = Usuario("usuario1@example.com", "usuario1")
    cadastro.Cadastrar_Usuario(usuario1)

# Executando a função Main
Main()
