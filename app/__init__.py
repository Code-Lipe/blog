from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# A instância do banco de dados é criada aqui, mas sem um app
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # A instância do banco de dados é vinculada ao app aqui
    db.init_app(app)

    # Importa e registra o Blueprint aqui
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app