from flask import Flask, render_template, request, redirect, url_for
import repositorio


app = Flask(__name__)
@app.route("/")
def home():
    dicionario = repositorio.retornar_personagens()
    return render_template("personagem.html", dados=dicionario)

@app.route("/test")
def test():
    dicionario = repositorio.retornar_personagens()
    return dicionario

@app.route("/personagem/<int:id>", methods=['GET', 'POST'])
def editar_personagem(id):

    if request.method == 'POST':
        if "excluir" in request.form:
            repositorio.remover_personagem(id)
            return redirect(url_for("home"))
        elif "salvar" in request.form:
            personagem = {}
            personagem['nome'] = request.form['nome']
            personagem['cla'] = request.form['cla']
            personagem['vila'] = request.form['vila']
            personagem['ocupacao'] = request.form['ocupacao']
            personagem['habilidades'] = request.form['habilidades']
            personagem['imagem'] = request.form['imagem']

            if id in repositorio.retornar_personagens().keys():
                repositorio.atualizar_personagem(id, personagem)

            return redirect(url_for("home"))
    else:

        personagem = repositorio.retornar_personagem(id)
        personagem['id'] = id
        return render_template("cadastro.html", **personagem)
    
@app.route("/personagem", methods=['GET', 'POST'])
def criar_personagem():
    if request.method == 'POST':
            personagem = {}
            personagem['nome'] = request.form['nome']
            personagem['cla'] = request.form['cla']
            personagem['vila'] = request.form['vila']
            personagem['ocupacao'] = request.form['ocupacao']
            personagem['habilidades'] = request.form['habilidades']
            personagem['imagem'] = request.form['imagem']
            repositorio.criar_personagem(**personagem)
            return redirect(url_for("home"))

    else:
        return render_template("cadastro.html", id=repositorio.gerar_id())

app.run(debug=True)