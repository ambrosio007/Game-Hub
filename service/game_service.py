from repository.game_repository import GameRepository
from model.game_model import Game

class GameService:
    @staticmethod
    def add_game(data):
        """Adiciona um novo jogo ao repositório."""
        game = Game(**data)
        GameRepository.add(game)
        return game

    @staticmethod
    def get_game_by_name(name):
        """Busca um jogo por nome."""
        return GameRepository.get_by_name(name)
    
    @staticmethod
    def get_game_by_id(game_id):
        """Busca um jogo por ID."""
        return GameRepository.get_by_id(game_id)
    
    @staticmethod
    def update_game(game_id, new_data):
        """Atualiza os dados de um jogo."""
        return GameRepository.update(game_id, new_data)
    
    @staticmethod
    def delete_game(game_id):
        """Deleta um jogo do repositório."""
        return GameRepository.delete(game_id)
    
    @staticmethod
    def list_all_games():
        """Lista todos os jogos disponíveis."""
        return GameRepository.load_all()