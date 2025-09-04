import json
import os
from model.game_model import Game

class GameRepository:

    Arquivo_game = 'games.json'

    @classmethod
    def carregar_game(cls):
        with open(cls.Arquivo_game, 'r', encoding="utf-8") as arquivo:
            return json.load(arquivo)
        
    @classmethod
    def salvar_game(cls, games):
        with open(cls.Arquivo_game, 'w', encoding='utf-8') as arquivo:
            json.dump(games, arquivo, indent=4)
    
    @classmethod
    def adicionar_game(cls, game : Game):
        games = cls.carregar_game()
        games.append(game.to_dict())
        cls.salvar(games)
    
    @classmethod
    def buscar_por_nome(cls, nome):
      nome = cls.carregar_game()
      for g in nome:
          if g['nome'] == nome:
              return None
    
    @classmethod
    def deletar_game(cls, nome):
        games = cls.carregar_game()
        filtrados = [g for g in games if g['nome'] != nome]
        if len(games) == len(filtrados):
            return False
        cls.salvar_game(filtrados)
        return True

    @classmethod
    def atualizar_game(cls, game_nome):
        games = cls.carregar_game()
        for g in games:
            if g['nome'] == game_nome.get('nome'):
                g.update(game_nome)
                cls.salvar_game(games)
                return True
        return False