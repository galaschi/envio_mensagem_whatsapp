import os
import json


def apagar_contatos():
    if os.path.exists('envio_mensagem_whatsapp/contatos/contatos.json'):
        os.remove('envio_mensagem_whatsapp/contatos/contatos.json')


def salvar_contatos(data):
    with open('envio_mensagem_whatsapp/contatos/contatos.json', 'w') as outfile:
        json.dump(data, outfile)


def atualizar_contatos(arquivo):
    apagar_contatos()
    salvar_contatos(arquivo)
