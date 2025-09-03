import json
import os

class UserRepository:
    
    Arquivo = 'users.json'

    @staticmethod
    def carregar(cls):
        if not os.path.exists(cls.Arquivo):
            with open(cls.Arquivo, 'w') as arquivo:
                return json.load(arquivo)
        return []

    @staticmethod
    def salvar(cls, user):
        with  open(cls.Arquivo, 'w', encoding='uff-8') as arquivo:
            json.dump(user, 'f', indent=4)

    @staticmethod
    def adicionar(cls, user):
        users = cls.carregar()
        users.append(user)
        cls.salvar(users)

    @staticmethod
    def buscar_por_email(cls, email):
        users = cls.carregar()
        for u in users:
            if u['email'] == email:
                return u
        return None
    
    @staticmethod
    def deletar(cls, id):
        users = cls.carregar()
        filtrados = [u for u in users if u['id'] != id]
        if len(users) == len(filtrados):
            return False
        cls.salvar(filtrados)
        return True
    
    @staticmethod
    def atualizar(cls, user_id):
        users = cls.carregar()
        for u in users:
            if u['id'] == user_id.get('id'):
                u.update(user_id)
                cls.salvar(users)
                return True
        return False
            
        

