from flask import Blueprint, redirect, render_template, request, jsonify

#create a login blueprint
user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/', methods=['GET'])
def index():
    return render_template("users/index.html", example = "user")

@user.route('/example', methods=['GET','POST'])
def something():
    return jsonify(request.form)
    