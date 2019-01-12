from flask import Flask

import webApp.views
import webApp.models

app = Flask(__name__)

# app.register_blueprint(webApp.views.login)
# app.register_blueprint(webApp.views.user)
app.register_blueprint(webApp.views.leaderboard)
app.register_blueprint(webApp.views.picture)

