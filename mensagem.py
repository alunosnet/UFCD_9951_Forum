from flask import Flask, render_template,request,redirect
from basedados import *
from datetime import date

def mensagem_responder():
    id = request.form.get("id")
    parametros = (id,)
    texto = DevolverSQL("SELECT * FROM Mensagem WHERE id=?",parametros)
    respostas = DevolverSQL("SELECT * FROM Mensagem WHERE id_mensagem_original=?",parametros)
    utilizadores = DevolverSQL("SELECT id,nome FROM Utilizador ORDER BY Nome")
    return render_template("mensagem/responder.html",mensagem=texto[0],registos=respostas,utilizadores=utilizadores)

def mensagem_listar():

    if request.method=="POST":
        #recolher os dados da mensagem
        texto = request.form.get("texto")
        id_utilizador = request.form.get("utilizador")
        #validar os dados
        if texto and id_utilizador:
            #adicionar à tabela das mensagens
            data_atual=date.today()
            sql="INSERT INTO Mensagem(id_utilizador,data_hora_mensagem,texto)VALUES(?,?,?)"
            parametros=(id_utilizador,data_atual,texto)
            ExecutarSQL(sql,parametros)
            mensagem="Mensagem enviada com sucesso"
        else:
            mensagem="Tem de preencher todos os campos"
    else:
        mensagem=""
    #consulta à bd para recolher todas as mensagens iniciais
    sql = "SELECT * FROM Mensagem WHERE id_mensagem_original is null"
    #TODO: join para acrescentar o nome do utilizador
    utilizadores = DevolverSQL("SELECT id,nome FROM Utilizador ORDER BY nome")
    dados = DevolverSQL(sql)
    return render_template("mensagem/index.html",utilizadores=utilizadores,registos=dados,mensagem=mensagem)