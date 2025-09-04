import uuid

class Jogo:
    def __init__(self, user_id, nome, desc, capa, plataforma1, plataforma2, plataforma3, jogo_id=None):
        self.user_id = user_id 
        self.jogo_id = jogo_id or str(uuid.uuid4())
        self.nome = nome
        self.desc = desc
        self.capa = capa
        self.plataforma1 = plataforma1
        self.plataforma2 = plataforma2
        self.plataforma3 = plataforma3

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'jogo_id': self.jogo_id,
            'nome': self.nome,
            'desc': self.desc,
            'capa': self.capa,
            'plataforma1': self.plataforma1,
            'plataforma2': self.plataforma2,
            'plataforma3': self.plataforma3,
        }