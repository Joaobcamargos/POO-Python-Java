# -*- coding: utf-8 -*-
"""
@author: joaobcamargos
:)
"""

from abc import ABC , abstractmethod

class User(ABC):
    users = []
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
    
    def save_database(self, file):
        with open(file, 'w') as f:
            for user in self.users:
                f.write(f"{user.name},{user.email}")
    
    @abstractmethod 
    def register(a, b, c):
        print('Registering')
    
class Employee(User):
    def __init__(self, role, name, password, email):
        super().__init__(name, password, email)
        self.role = role
    
    def register(self, a, b, c):
        if User.users.count(a) != 0:
            print('Username already registered ERROR!')
        else:
            name = a
            password = b
            email = c
            User.users.append(Employee(self.role, name, password, email))  
    
class Client(User):
    def __init__(self, type, name, password, email):
        super().__init__(name, password, email)
        self.type = type
    
    def register(self, a, b, c):
        if User.users.count(a) != 0:
            print('Username already registered ERROR!')
        else:
            name = a
            password = b
            email = c
            User.users.append(Employee(self.type, name, password, email))
        
               

employee = Employee("Developer", "john", "password123", "john@email.com")
employee.register("mary", "anotherpassword", "mary@email.com")

client = Client("Premium", "ana", "password456", "ana@email.com")
client.register("peter", "anotherpassword", "peter@email.com")

print("Registered users:")
for user in User.users:
    print(f"Name: {user.name}, Email: {user.email}")
