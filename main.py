from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy

# Configuração do Flask e Banco de Dados
app = Flask(__name__)
app.config['SECRET_KEY'] = "PALAVRA-SECRETA"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo do Banco de Dados
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

@app.route("/")
def home():
    return render_template("html/login.html")

@app.route("/login", methods=['POST'])
def login():
    usuario = request.form.get('nome')
    senha = request.form.get('senha')

    # CONSULTA INSEGURA: Sujeita a SQL Injection
    query = f"SELECT * FROM usuario WHERE nome = '{usuario}' AND senha = '{senha}'"
    result = db.session.execute(query).fetchone()

    if result:
        return render_template("html/acesso.html", nomeUsuario=result.nome)
    else:
        flash('Usuário ou senha invalidos')
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
