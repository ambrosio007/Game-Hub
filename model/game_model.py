class Jogo:
    def __init__(self, nome_g, descriçõa, capa, link):
        self.nome_g = nome_g
        self.descrição = descriçõa
        self.capa = capa
        self.link = link

    def to_dirct(self):
        return {

            'nome_g': self.nome_g,
            'descrição': self.descrição,
            'capa': self.capa,
            'link': self.link,

        }