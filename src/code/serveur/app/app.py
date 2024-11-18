from flask import Flask
from config import Configuration # importation de la classe de configuration

app = Flask(__name__)
# __name__ indique la racine de l'application pour retrouver les ressources

app.config.from_object(Configuration)