from flask import Flask, render_template

app = Flask(__name__)

# Lista de posts temporária
posts = [
    {'titulo': 'Meu Primeiro Post', 'autor': 'João'},
    {'titulo': 'Aprendendo Python', 'autor': 'Maria'}
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/posts/<int:post_id>")
def show_post(post_id):
    return f"Você está visualizando o post de ID {post_id}"


if __name__ == '__main__':
    app.run(debug=True)