from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

# Configuração do Flask e Banco de Dados
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo da Tabela
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

# Página de Login
@app.route("/")
def home():
    return """
    <form action="/login" method="POST">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome"><br><br>
        <label for="senha">Senha:</label>
        <input type="password" id="senha" name="senha"><br><br>
        <button type="submit">Entrar</button>
    </form>
    """

# Endpoint de Login (Vulnerável)
@app.route("/login", methods=["POST"])
def login():
    nome = request.form.get("nome")
    senha = request.form.get("senha")

    # Consulta SQL Vulnerável
    query = text(f"SELECT * FROM usuario WHERE nome='{nome}' AND senha='{senha}'")
    result = db.session.execute(query).fetchone()

    if result:
        return f"Bem-vindo, {result['nome']}!"
    else:
        return "Usuário ou senha inválidos."

# Função para criar o banco de dados
def criar_banco():
    with app.app_context():
        db.create_all()
        print("Banco de Dados Criado!")

# Função para popular o banco de dados com usuários iniciais
def popular_banco():
    with app.app_context():
        usuarios = [
            Usuario(nome="admin", senha="1234"),
            Usuario(nome="usuario", senha="senha123")
        ]
        db.session.add_all(usuarios)
        db.session.commit()
        print("Usuários adicionados ao banco de dados!")

if __name__ == '__main__':
    criar_banco()
    popular_banco()
    app.run(debug=True)
