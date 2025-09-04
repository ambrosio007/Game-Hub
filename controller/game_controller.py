from flask import Blueprint, request, jsonify, render_template, redirect, session, url_for
from service.game_service import GameService

game_bp = Blueprint('game', _name_)


# Rota para a página de listagem de jogos (HTML)
@game_bp.route("/games")
def list_games_page():
    games = GameService.list_all_games()
    return render_template("games.html", games=games)

# Rota para a página de adicionar jogo (HTML)
@game_bp.route("/games/add")
def add_game_page():
    if 'user_id' not in session:
        return redirect(url_for('user.login_get'))
    return render_template("add_game.html")

# Rota da API para adicionar um novo jogo (POST)
@game_bp.route("/games/add", methods=["POST"])
def add_game():
    if 'user_id' not in session:
        return jsonify({"error": "Autenticação necessária."}), 401

    data = request.get_json()

    required_fields = ["game_name", "release_year", "purchase_link"]
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Campos obrigatórios ausentes: game_name, release_year, purchase_link."}), 400

    game_data = {
        "game_name": data["game_name"],
        "description": data.get("description"),
        "release_year": data["release_year"],
        "cover_image": data.get("cover_image"),
        "purchase_link": data["purchase_link"],
        "user_id": session['user_id']  # Associa o jogo ao usuário logado
    }
    
    game = GameService.add_game(game_data)


    if game:
        # Assumindo que o objeto 'game' retornado pelo serviço tem um atributo 'game_name'
        return jsonify({"message": f"Jogo {game.game_name} cadastrado com sucesso!"}), 201
    return jsonify({"error": "Não foi possível cadastrar o jogo."}), 500

# Rota da API para listar todos os jogos (JSON)
@game_bp.route("/games/json")
def list_games_json():
    games = GameService.list_all_games()
    return jsonify(games)


# Rota da API para deletar um jogo (DELETE)
@game_bp.route("/games/<id>", methods=["DELETE"])
def delete_game(id):

    if 'user_id' not in session:
        return jsonify({"error": "Autenticação necessária."}), 401

    if GameService.delete_game(id):
        return jsonify({"message": "Jogo deletado com sucesso."})

    return jsonify({"error": "Jogo não encontrado ou você não tem permissão."}), 404

# Rota da API para atualizar um jogo (PUT)
@game_bp.route("/games/<id>", methods=["PUT"])
def update_game(id):

    if 'user_id' not in session:
        return jsonify({"error": "Autenticação necessária."}), 401

    game_edit = request.get_json()
    if not game_edit:
        return jsonify({"error": "Corpo da requisição vazio."}), 400

    if GameService.update_game(id, game_edit):
        return jsonify({"message": "Jogo atualizado com sucesso."})

    return jsonify({"error": "Jogo não encontrado ou você não tem permissão."}), 404
from service.game_service import GameService