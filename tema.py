from flask import Flask, render_template,request,redirect
from basedados import *

def tema_adicionar():
    if request.method=="GET":
        return render_template('tema/adicionar.html')
    if request.method=="POST":
        #recolher os dados do form
        nome = request.form.get("nome")

        #validar os dados
        if not nome:
            return render_template('tema/adicionar.html',mensagem="Tem de preencher todos os campos")
        
        #adicionar a bd
        sql="INSERT INTO Tema(nome, estado) values(?,?)"
        parametros=(nome,1)
        ExecutarSQL(sql,parametros)
        #redirecionar
        return redirect('/tema/listar')

def tema_listar():
    sql = "SELECT * FROM Tema"
    dados = DevolverSQL(sql)
    return render_template("Tema/listar.html",registos=dados)

def tema_apagar():
    pass