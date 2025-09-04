from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Dados que serão retornados como JSON.
dados_jogos = [
    {
        "nome": "God of War ragnarok",
        "image": "../static/Images/capa-gow-ragnarok.webp"
    },
    {
        "nome": "Grand Theft Auto VI",
        "image": "../static/Images/capa-gta6.jpg"
    },
    {
        "nome": "Minecraft",
        "image": "../static/Images/capa-minecraft.jpg"
    },
    {
        "nome": "Mortal Kombat 1",
        "image": "../static/Images/capa-mk1.webp"
    }
]

# Rota para retornar o JSON
@app.route('/jogos.json')
def get_jogos_json():
    # O jsonify converte a lista de dicionários para uma resposta JSON
    return jsonify(dados_jogos)

# Rota para o HTML

# Rota para a página de jogos.
@app.route('/jogos')
def home():
    return render_template('jogos.html')

if __name__ == '__main__':
    app.run(debug = True)