import bcrypt
from repository.user_repository import UserRepository
from model.user_model import User

class UserService:

    @staticmethod
    def cadastrar(dados):
        user = User(**dados)
        UserRepository.adicionar(user)
        return user
    
    @staticmethod
    def autenticar(usuario, senha):
        user = UserRepository.buscar_por_usuario(usuario)
        if user and bcrypt.checkpw(senha.encode('utf-8'), user['senha'].encode('utf-8')):
            return user
        return None
    
    @staticmethod
    def atualizar(user_id):
        return UserRepository.atualizar(user_id)
    
    @staticmethod
    def deletar(user_id):
        return UserRepository.deletar(user_id)
    
    @staticmethod
    def listar():
        return UserRepository.carregar()