from flask import render_template, redirect, url_for, request
from envio_mensagem_whatsapp import disparo_mensagem as msg, app
from envio_mensagem_whatsapp.contatos import importar_contatos
import pandas


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home_page():
    return render_template('home.html')


@app.route("/enviar_mensagem", methods=['GET', 'POST'])
def enviar_mensagem():
    mensagem = request.form['mensagem']
    msg.disparar_mensagem(mensagem)
    return redirect(url_for('home_page'))


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    contatos = pandas.read_excel(request.files['upload-file'])
    importar_contatos.atualizar_contatos(contatos.to_dict())

    return redirect(url_for('home_page'))
