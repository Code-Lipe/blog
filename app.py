from flask import Flask, render_template, redirect, url_for
from extensions import db
from models import Post

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do banco de dados
db.init_app(app)

@app.route("/")
def index():
    posts_do_db = Post.query.all()
    return render_template("index.html", posts=posts_do_db)

@app.route("/posts/<int:post_id>")
def show_post(post_id):
    post_do_db = Post.query.get_or_404(post_id)
    return render_template("post.html", post=post_do_db)

@app.route("/delete/<int:post_id>", methods=['POST'])
def delete_post(post_id):
    post_a_deletar = Post.query.get_or_404(post_id)
    db.session.delete(post_a_deletar)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)