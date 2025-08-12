from flask import render_template, redirect, url_for
from . import db
from .models import Post
from flask import current_app

@current_app.route("/")
def index():
    posts_do_db = Post.query.all()
    return render_template("index.html", posts=posts_do_db)

@current_app.route("/posts/<int:post_id>")
def show_post(post_id):
    post_do_db = Post.query.get_or_404(post_id)
    return render_template("post.html", post=post_do_db)

@current_app.route("/delete/<int:post_id>", methods=['POST'])
def delete_post(post_id):
    post_a_deletar = Post.query.get_or_404(post_id)
    db.session.delete(post_a_deletar)
    db.session.commit()
    return redirect(url_for('index'))