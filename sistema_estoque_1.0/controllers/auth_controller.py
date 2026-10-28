from flask import (Blueprint, render_template, request, redirect, session)
from services.auth_service import autenticar
# Blueprint: REgistrar rotas fora do app.py
auth_bp = Blueprint("auth", __name__)
#Criar a rota da tela inicial localhost:5000
@auth_bp.route("/", methods=["GET"])
def loguin():
    return render_template("loguin.html")
# Criar a roque que recebe o formulario de loguin
@auth_bp.route("/login", methods=["POST"])
def realizar_login():
    loguin = request.form["login"]
    senha = request.form["senha"]
    usuario = autenticar(loguin, senha)
    if usuario is None:
        return render_template(
            "login.html", erro = "Login ou senha invalidos"
            )
    session["usuario_id"] = usuario["id"]
    session["nome"] = usuario["nome"]
    session["perfil"] = usuario["perfil"] 
    return redirect("/produtos")