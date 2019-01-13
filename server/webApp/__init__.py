from flask import Flask
import os
import webApp.views

app = Flask(__name__)

app.register_blueprint(webApp.views.picture)

path = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER  = os.path.join(path, "images")
print(UPLOAD_FOLDER)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER



