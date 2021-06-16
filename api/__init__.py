from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_login import LoginManager



#from sqlobject import *
app = Flask(__name__, instance_relative_config=True)

mail= Mail(app)
app.config.from_object('config.Config')
# for ele in app.config:
#     print(ele,app.config[ele])
mail = Mail(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager = LoginManager(app)


db = SQLAlchemy(app)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .models import HealthUser



@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return HealthUser.query.get(int(user_id))


from api import routes
