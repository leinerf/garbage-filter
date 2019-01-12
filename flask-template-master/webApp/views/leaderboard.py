from flask import Blueprint, redirect, render_template, request, jsonify
import json

leaderboard = Blueprint('leaderboard', __name__, url_prefix='/leaderboard')

@leaderboard.route('/', methods=["GET"])
def index():
    return jsonify({"leaderboard": "example"})