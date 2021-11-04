from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

#Configurações:

#1 - Vincular com flask:
app = Flask(__name__)
CORS(app) #aplicar o cross domain
#2 - Caminho do arquivo do banco de dados 
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, '4thenature.db')
#3 - Informar que o banco de dados vai ser criado no arquivobd
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + arquivobd
#4 - Remover warnings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#5 - Cria vínculo com a biblioteca SQLAlchemy
db = SQLAlchemy(app)
