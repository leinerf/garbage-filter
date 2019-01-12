from flask import Blueprint, redirect, render_template, request, jsonify
import json

picture = Blueprint('picture', __name__, url_prefix='/picture')

@picture.route('/', methods=["GET"])
def index():
    return jsonify({"picture": "example"})