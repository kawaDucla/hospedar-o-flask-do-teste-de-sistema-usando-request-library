from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

URL = "https://teste-de-sistemas-default-rtdb.firebaseio.com/.json"


@app.route("/")
def index():
    resposta = requests.get(URL)
    dados = resposta.json() or {}
    return render_template("index.html", dados=dados)

@app.route("/add", methods=["POST"])
def add():
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    novo = {"Nome": nome, "Sobrenome": sobrenome}
    requests.post(URL, json=novo)
    return redirect("/")

@app.route("/delete/<id>")
def delete(id):
    requests.delete(f"https://teste-de-sistemas-default-rtdb.firebaseio.com/{id}.json")
    return redirect("/")


@app.route("/edit/<id>")
def edit(id):
    resposta = requests.get(f"https://teste-de-sistemas-default-rtdb.firebaseio.com/{id}.json")
    dados = resposta.json()
    return render_template("edit.html", id=id, dados=dados)

@app.route("/update/<id>", methods=["POST"])
def update(id):
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    novo = {"Nome": nome, "Sobrenome": sobrenome}
    requests.patch(f"https://teste-de-sistemas-default-rtdb.firebaseio.com/{id}.json", json=novo)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
