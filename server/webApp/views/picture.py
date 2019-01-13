from flask import Blueprint, redirect, render_template, request, jsonify
from ..submitImage import sendImageToBucket
from werkzeug import secure_filename
from ..labelImage import getImageLabel
import os
picture = Blueprint('picture', __name__, url_prefix='/picture')

@picture.route('/', methods=["POST","GET"])
def index():
    if request.method == 'POST':
        print("it went here")
        f = request.files['photo']
        filename = secure_filename(f.filename)
        total_file_path = os.path.join("/Users/frenielzabala/projects/trashMe2.0/server/webApp/images", filename)
        f.save(total_file_path)
        sendImageToBucket(total_file_path)
        return jsonify({"message": getImageLabel()})
    return jsonify({"label":"something", "score": "something" })