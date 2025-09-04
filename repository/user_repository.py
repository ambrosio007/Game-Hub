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
        print(users[0])
        cls.salvar(users)

    @classmethod
    def buscar_por_usuario(cls, usuario):
        users = cls.carregar()
        for u in users:
            if u['usuario'] == usuario:
                return u
        return None
    
    @classmethod
    def deletar(cls, id):
        users = cls.carregar()
        filtrados = [u for u in users if u['id'] != id]
        if len(users) == len(filtrados):
            return False
        cls.salvar(filtrados)
        return True
    
    @classmethod
    def atualizar(cls, user_id):
        users = cls.carregar()
        for u in users:
            if u['id'] == user_id.get('id'):
                u.update(user_id)
                cls.salvar(users)
                return True
        return False
            
        

