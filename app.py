from flask import Flask, render_template, request, redirect, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "segredo"


def conectar():
    return sqlite3.connect("database.db")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        senha = request.form["senha"]

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM usuarios WHERE email=? AND senha=?",
            (email, senha)
        )

        usuario = cursor.fetchone()
        conexao.close()

        if usuario:
            session["usuario"] = email
            return redirect("/painel")

        else:
            return "Usuário ou senha incorretos"

    return render_template("login.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":

        email = request.form.get("email")
        senha = request.form.get("senha")

        if not email or not senha:
            return "Preencha todos os campos!", 400

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO usuarios (email, senha) VALUES (?, ?)",
            (email, senha)
        )

        conexao.commit()
        conexao.close()

        return redirect("/login")

    return render_template("cadastro.html")

@app.route("/painel")
def painel():

    if "usuario" not in session:
        return redirect("/login")

    return render_template("painel.html")


@app.route("/entrada")
def entrada():

    if "usuario" not in session:
        return redirect("/login")

    usuario = session["usuario"]
    data = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%H:%M:%S")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO pontos (usuario, data, hora, tipo) VALUES (?, ?, ?, ?)",
        (usuario, data, hora, "entrada")
    )

    conexao.commit()
    conexao.close()

    return "Entrada registrada com sucesso"


@app.route("/saida")
def saida():

    if "usuario" not in session:
        return redirect("/login")

    usuario = session["usuario"]
    data = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%H:%M:%S")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO pontos (usuario, data, hora, tipo) VALUES (?, ?, ?, ?)",
        (usuario, data, hora, "saida")
    )

    conexao.commit()
    conexao.close()

    return redirect("/painel")


@app.route("/historico")
def historico():

    if "usuario" not in session:
        return redirect("/login")

    usuario = session["usuario"]

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT data, hora, tipo FROM pontos WHERE usuario=? ORDER BY id DESC",
        (usuario,)
    )

    registros = cursor.fetchall()
    conexao.close()

    return render_template("historico.html", registros=registros)


@app.route("/logout")
def logout():

    session.pop("usuario", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)