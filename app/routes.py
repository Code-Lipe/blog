from flask import Blueprint, render_template, redirect, url_for
from . import db
from .models import Post

# Cria um Blueprint chamado 'main'
main = Blueprint('main', __name__)

@main.route("/")
def index():
    posts_do_db = Post.query.all()
    return render_template("index.html", posts=posts_do_db)

@main.route("/posts/<int:post_id>")
def show_post(post_id):
    post_do_db = Post.query.get_or_404(post_id)
    return render_template("post.html", post=post_do_db)

@main.route("/delete/<int:post_id>", methods=['POST'])
def delete_post(post_id):
    post_a_deletar = Post.query.get_or_404(post_id)
    db.session.delete(post_a_deletar)
    db.session.commit()
    return redirect(url_for('main.index'))