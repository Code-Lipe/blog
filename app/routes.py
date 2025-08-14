from flask import Blueprint, render_template, redirect, url_for, flash
from . import db
from .models import Post
from .forms import PostForm

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
    flash('Postagem excluída com sucesso!', 'danger')
    return redirect(url_for('main.index'))

@main.route("/novo-post", methods=['GET', 'POST'])
def novo_post():
    form = PostForm ()
    if form.validate_on_submit():
        novo_post = Post(
            titulo=form.titulo.data,
            autor=form.autor.data,
            conteudo=form.conteudo.data
        )
        db.session.add(novo_post)
        db.session.commit()
        flash('Sua postagem foi criada com sucesso!', 'success')
        return redirect(url_for('main.index'))

    return render_template('novo_post.html', form=form)