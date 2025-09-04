import json
import os
from model.user_model import User

class UserRepository:
    
    Arquivo = 'users.json'

    @classmethod
    def carregar(cls):
        with open(cls.Arquivo, 'r', encoding="utf-8") as arquivo:
            return json.load(arquivo)

    @classmethod
    def salvar(cls, user):
        with open(cls.Arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(user, arquivo, indent=4)

    @classmethod
    def adicionar(cls, user : User):
        users = cls.carregar()
        users.append(user.to_dict())
        cls.salvar(users)

    @classmethod
    def buscar_por_usuario(cls, usuario):
        users = cls.carregar()
        for u in users:
            if u['usuario'] == usuario:
                return u
        return None

            
        

