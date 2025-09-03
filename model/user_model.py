import uuid
import bcrypt

class User:
    def __init__(self, nome, usuario, email, senha, id=None):
        self.id = id or str(uuid.uuid4())
        self.nome = nome
        self.usuario = usuario
        self.email = email
        self.senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def to_dict(self):
        return {

            'id': self.id, 
            'nome': self.nom, 
            'usuario': self.usuario, 
            'email': self.email, 
            'senha': self.senha, 
        }