import json
import os
from model.game_model import Jogo

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
    def adicionar_game(cls, game : Jogo):
        games = cls.carregar_game()
        games.append(game.to_dict())
        cls.salvar_game(games)

    
    @classmethod
    def deletar_game(cls, id):
        games = cls.carregar_game()
        filtrados = [g for g in games if g['jogo_id'] != id]
        if len(games) == len(filtrados):
            return False
        cls.salvar_game(filtrados)
        return True