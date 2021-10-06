from flask import Flask

app = Flask(__name__)

from envio_mensagem_whatsapp import routes

