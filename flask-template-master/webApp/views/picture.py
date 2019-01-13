from flask import Blueprint, redirect, render_template, request, jsonify
from ..imageConverter import something


picture = Blueprint('picture', __name__, url_prefix='/picture')

@picture.route('/', methods=["POST","GET"])
def index():
    return jsonify({"label":"something", "score": "something" })