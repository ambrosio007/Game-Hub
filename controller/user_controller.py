from flask import Blueprint, request, jsonify, render_template, redirect, session, url_for
from service.user_service import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route("/")
def cad():
    return render_template("register.html")

@user_bp.route("/login")
def login_get():
    return render_template("login.html")

@user_bp.route("/cadastro")
def cadastro_get():
    return render_template("register.html")

@user_bp.route("/home")
def home():
    if not session:
        return render_template("register.html")
    return render_template("home.html")

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
        return jsonify({"mensagem": f"Usuário {user['nome']} logado com sucesso!"})
    return jsonify({"erro": "Email ou senha incorretos."})

@user_bp.route("/logout")
def logout():
    session.clear()
    return render_template("register.html")

@user_bp.route("/user/json")
def buscar_usuarios_json():
    if "id_user" not in session:
        return jsonify({"error": "Cadastre para acessar essa página.",
                        "login_url": url_for("user.login")
                        }), 401
    return jsonify(UserService.buscar_user())

@user_bp.route("/user")
def buscar_users():
    if "id_user" not in session:
        return jsonify({"error": "Cadastre para acessar essa página.",
                        "login_url": url_for("user.login")
                        }), 401
    users = UserService.buscar_user()
    return render_template("users.html", users=users)
    
@user_bp.route("/user/<id>", methods=["DELETE"])
def deletar_user(id):
    if session.get("id_user") != id:
        return jsonify({"error": "Você não tem permissão para deletar este usuário."}), 403
    if UserService.deletar_user(id):
        session.clear()
        return jsonify({"message": "Usuário deletado com sucesso."})
    return jsonify({"error": "Usuário não encontrado."}), 404

@user_bp.route("/user/", methods=["PUT"])
def atualizar_user():
    if "id_user" not in session:
        return jsonify({"error": "Você não tem permissão para alterar este usuário."}), 403
    
    user_edit = request.get_json()
    if UserService.atualizar_user(user_edit):
        return jsonify({"message": "Usuário atualizado com sucesso."})
    return jsonify({"error": "Usuário não encontrado."}), 404
