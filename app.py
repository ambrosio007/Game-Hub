from flask import Flask
from controller.user_controller import user_bp
from controller.game_controller import game_bp

app = Flask(_name_)
app.secret_key = 'sua_chave_secreta_aqui '

app.register_blueprint(user_bp)
app.register_blueprint(game_bp)

if _name_ == '_main_':
    app.run(debug=True)