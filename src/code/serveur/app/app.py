from flask import Flask
from flask_talisman import Talisman
from config import Configuration # importation de la classe de configuration

app = Flask(__name__)

#talisman = Talisman(app, force_https=True)

app.config.from_object(Configuration)