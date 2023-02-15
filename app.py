from flask import Flask,render_template

app = Flask(__name__)
#POSTS MOC 

posts =[
    {
        "titulo" : "Post 1",
        "texto": "Meu primeiro post"
    },
    {
        "titulo" : "Post 2",
        "texto": "Meu segundo post"
    },
    {
        "titulo" : "Post 3",
        "texto": "Meu terceiro post"
    },
]

@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas=posts)

   