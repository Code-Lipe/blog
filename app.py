from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do banco de dados
db = SQLAlchemy(app)

# Lista de posts temporária
posts = [
    {'id': 1, 'titulo': 'Meu Primeiro Post', 'autor': 'Harry', 'conteudo': 'O conteúdo do meu primeiro post é este aqui. É sobre...'},
    {'id': 2, 'titulo': 'Aprendendo Python', 'autor': 'Hermione', 'conteudo': 'Neste post, vou falar sobre como começar a programar em Python.'}
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/posts/<int:post_id>")
def show_post(post_id):
    post = None
    for p in posts:
        if p['id'] == post_id:
            post = p
            break
    return render_template("post.html", post=post)


if __name__ == '__main__':
    app.run(debug=True)