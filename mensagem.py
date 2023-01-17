from flask import Flask, render_template,request,redirect
from basedados import *

def mensagem_listar():
    #consulta à bd para recolher todas as mensagens iniciais
    sql = "SELECT * FROM Mensagem WHERE id_mensagem_original is null"
    #TODO: join para acrescentar o nome do utilizador
    if request.method=="POST":
        #recolher os dados da mensagem
        texto = request.form.get("texto")
        id_utilizador = request.form.get("utilizador")
        #validar os dados
        if not texto or not id_utilizador:
            return render_template("mensagem/index.html",mensagem="Tem de preencher todos os campos")

        #adicionar à tabela das mensagens
        data_atual=date.today()
        sql="INSERT INTO Utilizador(id_utilizador,data_mensagem,texto)VALUES(?,?,?)"
        parametros=(id_utilizador,data_atual,texto)
        ExecutarSQL(sql,parametros)


    utilizadores = DevolverSQL("SELECT id,nome FROM Utilizador ORDER BY nome")
    dados = DevolverSQL(sql)
    return render_template("mensagem/index.html",utilizadores=utilizadores,registos=dados)