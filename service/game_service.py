from repository.game_repository import GameRepository
from model.game_model import Jogo

class GameService:
    @staticmethod
    def add_game(data):
        """Adiciona um novo jogo ao repositório."""
        game = Jogo(**data)
        GameRepository.adicionar_game(game)
        return game   
    
    @staticmethod
    def delete_game(game_id):
        """Deleta um jogo do repositório."""
        return GameRepository.deletar_game(game_id)
    