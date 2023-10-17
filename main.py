from flask import Flask, render_template
import repositorio

app = Flask(__name__)
@app.route("/")
def home():
    dicionario = repositorio.retornar_personagens()
    return render_template("personagem.html", dados = dicionario)

app.run(debug=True)