from flask import Flask
from controller.user_controller import user_bp
from controller.game_controller import game_bp

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui '

app.register_blueprint(user_bp)
app.register_blueprint(game_bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)