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

    return redirect("/sucesso/entrada")


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

    return redirect("/sucesso/saida")


@app.route("/sucesso/<tipo>")
def sucesso(tipo):
    if "usuario" not in session:
        return redirect("/login")
    return render_template("sucesso.html", tipo=tipo)


@app.route("/historico")
def historico():

    if "usuario" not in session:
        return redirect("/login")

    usuario = session["usuario"]
    data_inicio = request.args.get("data_inicio")
    data_fim = request.args.get("data_fim")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT data, hora, tipo FROM pontos WHERE usuario=? ORDER BY id DESC",
        (usuario,)
    )
    todos = cursor.fetchall()
    conexao.close()

    if data_inicio and data_fim:
        di = datetime.strptime(data_inicio, "%Y-%m-%d")
        df = datetime.strptime(data_fim, "%Y-%m-%d")
        registros = [
            r for r in todos
            if di <= datetime.strptime(r[0], "%d/%m/%Y") <= df
        ]
    else:
        registros = todos

    return render_template("historico.html", registros=registros, data_inicio=data_inicio or "", data_fim=data_fim or "")


@app.route("/logout")
def logout():

    session.pop("usuario", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)