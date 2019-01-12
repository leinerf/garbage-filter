from flask import Blueprint, redirect, render_template, request, jsonify
import json
#create a login blueprint
login = Blueprint('login', __name__, url_prefix='/login')


@login.route('/', methods=['GET', 'POST'])
def index():
    print(request.method)
    if(request.method == "POST"):        
        return jsonify(request.form)
    
    elif(request.method == "GET"):
        return render_template("login/index.html", example = login)

