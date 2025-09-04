from flask import Blueprint, request, jsonify, render_template, redirect, session, url_for
from service.user_service import UserService
import json

user_bp = Blueprint('user', __name__)

@user_bp.route("/")
def cad():
    return render_template("cadastro.html")

@user_bp.route("/login")
def login_get():
    return render_template("login.html")

@user_bp.route("/cadastro")
def cadastro_get():
    return render_template("cadastro.html")

@user_bp.route("/home")
def home():
    if not session:
        return redirect(url_for('user.login_get'))
    
    with open("games.json", "r", encoding="utf-8") as archive:
        jogos = json.load(archive)
    
    return render_template("home.html", jogos=jogos)

@user_bp.route("/cadastro", methods=["POST"])
def cadastrar_user():
    json = request.get_json()

    dados = {
        "nome": json["nome"],
        "usuario": json["usuario"],
        "email": json["email"],
        "senha": json["senha"],
    }
    user = UserService.cadastrar(dados)

    if user:
        return jsonify({"mensagem": f"Usuário {dados['nome']} cadastrado com sucesso!"})
    
    return jsonify({"erro": "Algo deu errado, tente novamente!"})

@user_bp.route("/login", methods=["POST"])
def login():
    json = request.get_json()
    usuario = json["usuario"]
    senha = json["senha"]

    user = UserService.autenticar(usuario, senha)
    if user:
        session['user_id'] = user["id"]
        session['user'] = user["usuario"]
        return jsonify({"mensagem": f"Usuário {user['nome']} logado com sucesso!"})
    return jsonify({"erro": "Email ou senha incorretos."})

@user_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('user.login_get'))

