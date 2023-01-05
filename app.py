from flask import Flask, render_template,request,redirect
from basedados import *

tabela_utilizador="create table if not exists utilizador(id integer primary key autoincrement, nome text, email text, palavra_passe text, estado integer)"
tabela_mensagem="create table if not exists mensagem(id integer primary key autoincrement, texto text, data_hora_mensagem numeric, id_utilizador integer references utilizador(id), id_mensagem_original integer references mensagem(id))"

ExecutarSQL(tabela_utilizador)
ExecutarSQL(tabela_mensagem)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/utilizador/registar',methods=["GET","POST"])
def utilizador_registar():
    if request.method=="GET":
        return render_template('utilizador/registar.html')
    if request.method=="POST":
        #recolher os dados do form
        nome = request.form.get("nome")
        email = request.form.get("email")
        palavra_passe = request.form.get("palavra_passe")
        #validar os dados
        if not nome or not email or not palavra_passe:
            return render_template('utilizador/registar.html',mensagem="Tem de preencher todos os campos")
        
        sql="SELECT * FROM Utilizador WHERE email=?"
        parametros=(email,)
        dados = DevolverSQL(sql,parametros)
        if dados:
            return render_template('utilizador/registar.html',mensagem="O email já existe")
        #adicionar a bd
        sql="INSERT INTO Utilizador(nome, email, palavra_passe, estado) values(?,?,?,?)"
        parametros=(nome,email,palavra_passe,1)
        ExecutarSQL(sql,parametros)
        #redirecionar
        return redirect('/utilizador/listar')

@app.route('/utilizador/listar')
def utilizador_listar():
    #consultar a bd para obter a lista de utilizadores
    sql = "SELECT * FROM Utilizador"
    dados = DevolverSQL(sql)
    return render_template('utilizador/listar.html',registos=dados)

@app.route('/utilizador/apagar',methods=["POST"])
def utilizador_apagar():
    #recolher o id do utilizador a apagar
    id = request.form.get("id")
    #consulta à bd para ter os dados do utilizador
    sql = "SELECT * FROM Utilizador WHERE id=?"
    parametros=(id,)
    dados = DevolverSQL(sql,parametros)
    #mostrar a página para confirmar o apagar
    return render_template("utilizador/apagar.html",registo=dados[0])

@app.route("/utilizador/apagar_confirmado",methods=["POST"])
def utilizador_apagar_confirmado():
    #recolher o id do utilizador a apagar
    id = request.form.get("id")
    #apagar da bd
    sql = "DELETE FROM Utilizador WHERE id=?"
    parametros=(id,)
    ExecutarSQL(sql,parametros)
    #redirecionar para utilizador/listar
    return redirect("/utilizador/listar")

#rota para editar

app.run()