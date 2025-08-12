from extensions import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(50), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Post {self.id}>'
