from flask import Flask, render_template,request,redirect
from basedados import *
import utilizador
import tema

#Criar a bd e as tabelas
tabela_utilizador="create table if not exists utilizador(id integer primary key autoincrement, nome text, email text, palavra_passe text, estado integer)"
tabela_mensagem="create table if not exists mensagem(id integer primary key autoincrement, texto text, data_hora_mensagem numeric, id_utilizador integer references utilizador(id), id_mensagem_original integer references mensagem(id))"
tabela_tema="create table if not exists tema(id integer primary key autoincrement, nome text, estado integer)"

ExecutarSQL(tabela_utilizador)
ExecutarSQL(tabela_mensagem)
ExecutarSQL(tabela_tema)

#Criar a aplicação Flask
app = Flask(__name__)

#Rotas/urls do site
@app.route('/')
def index():
    return render_template('index.html')

#rotas do tema
@app.route('/tema/adicionar',methods=["GET","POST"])
def tema_adicionar():
    return tema.tema_adicionar()
    
@app.route('/tema/listar')
def tema_listar():
    return tema.tema_listar()

@app.route('/tema/apagar',methods=["POST"])
def tema_apagar():
    return tema.tema_apagar()

#Rotas do utilizador
@app.route('/utilizador/registar',methods=["GET","POST"])
def utilizador_registar():
    return utilizador.utilizador_registar()

@app.route('/utilizador/listar')
def utilizador_listar():
    return utilizador.utilizador_listar()

@app.route('/utilizador/apagar',methods=["POST"])
def utilizador_apagar():
    return utilizador.utilizador_apagar()

@app.route("/utilizador/apagar_confirmado",methods=["POST"])
def utilizador_apagar_confirmado():
    return utilizador.utilizador_apagar_confirmado()

#rota para editar
@app.route("/utilizador/editar",methods=["POST"])
def utilizador_editar():
    return utilizador.utilizador_editar()

#rota para atualizar dados
@app.route("/utilizador/editar_confirmado",methods=["POST"])
def utilizador_editar_confirmado():
    return utilizador.utilizador_editar_confirmado()

app.run()