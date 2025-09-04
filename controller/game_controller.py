from flask import Blueprint, request, jsonify, render_template, redirect, session, url_for
from service.game_service import GameService
import os

game_bp = Blueprint('game', __name__)

capas_path = 'static/capas/'

if not os.path.exists(capas_path):
    os.makedirs(capas_path)

# Rota da API para adicionar um novo jogo (POST)
@game_bp.route("/games/add", methods=["POST"])
def add_game():
    if 'user_id' not in session:
        return redirect('user.login_get')

    nome = request.form.get('nome')
    desc = request.form.get('desc')
    plataforma1 = request.form.get('plataforma1')
    plataforma2 = request.form.get('plataforma2')
    plataforma3 = request.form.get('plataforma3')

    capa = request.files.get('imagem')

    if capa:
        capa_nome = os.path.basename(capa.filename)
        capa_caminho = os.path.join(capas_path, capa_nome)
        capa.save(capa_caminho)
        capa_caminho = os.path.join("/capas/", capa_nome)

    jogo = {"user_id": session['user_id'],
            "nome": nome,
            "desc": desc,
            "plataforma1": plataforma1,
            "plataforma2": plataforma2,
            "plataforma3": plataforma3,
            "capa": capa_caminho
            }
    
    status = GameService.add_game(jogo)

    if status:
        # Assumindo que o objeto 'game' retornado pelo serviço tem um atributo 'game_name'
        return jsonify({"mensagem": f"{status.nome} cadastrado com sucesso!"})
    # return jsonify({"error": "Não foi possível cadastrar o jogo."}), 500


# Rota da API para deletar um jogo (DELETE)
@game_bp.route("/games/<id>", methods=["DELETE"])
def delete_game(id):



    if GameService.delete_game(id):
        return jsonify({"mensagem": "Jogo deletado com sucesso."})

    return jsonify({"erro": "Jogo não encontrado ou você não tem permissão."}), 404
