from flask import Flask
import os

os.chmod('envio_mensagem_whatsapp', 755)
app = Flask(__name__)

from envio_mensagem_whatsapp import routes

