from flask import Flask, render_template, request, redirect, url_for, session, flash, g, abort
import sqlite3

app = Flask(__name__)
SECRET_KEY = "pudim"
DATABASE = "blog.bd"
app.config.from_object(__name__)

# POSTS MOCK
posts = [
    {
        "titulo": "Post 1",
        "texto": "Meu primeiro Post"
    },
    {
        "titulo": "Post 2",
        "texto": "Olha eu aqui de novo"
    },
       {
        "titulo": "Post 3",
        "texto": "Novo Post"
    }
]
# USER MOCKS
USERNAME = "admin"
PASSWORD = "admin"

def conectar_bd():
    return sqlite3.connect(DATABASE)

@app.before_request
def pre_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def encerrar_requisicao(exception):
    g.bd.close()


@app.route('/')
def exibir_entradas():
    #pegar posts no banco
    return render_template("exibir_entradas.html", entradas=posts)
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cursor = g.bd.execute(sql)
    entradas = [{"titulo": titulo, "texto": texto} for titulo, texto in cursor.fetchall()]
    return render_template("exibir_entradas.html", entradas=entradas)

@app.route('/inserir', methods=["POST"])
def inserir_entradas():
    novo_post = {
        "titulo": request.form['titulo'],
        "texto": request.form['texto']
    }
    posts.append(novo_post)  
    if not session['logado']:
        abort(401)
    sql = "INSERT INTO entradas(titulo, texto) VALUES (?, ?)"
    g.bd.execute(sql, [request.form['titulo'], request.form['texto']])
    g.bd.commit()
    flash("Novo Post criado com sucesso!")
    return redirect(url_for('exibir_entradas'))