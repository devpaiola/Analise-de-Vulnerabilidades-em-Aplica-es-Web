from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configuração do Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo da Tabela
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

# Função para criar e popular o banco de dados
def criar_e_popular_banco():
    with app.app_context():
        # Criação das tabelas
        db.create_all()

        # Dados de exemplo
        usuarios = [
            Usuario(nome="admin", senha="1234"),
            Usuario(nome="usuario", senha="senha123"),
            Usuario(nome="test", senha="teste123"),
        ]

        # Adicionar ao banco de dados
        db.session.add_all(usuarios)
        db.session.commit()
        print("Banco de dados criado e populado com sucesso!")

if __name__ == "__main__":
    criar_e_popular_banco()
