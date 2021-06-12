from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message




#from sqlobject import *
app = Flask(__name__, instance_relative_config=True)

mail= Mail(app)
app.config.from_object('config.Config')
# for ele in app.config:
#     print(ele,app.config[ele])
mail = Mail(app)


app.config.from_object('config')

db = SQLAlchemy(app)


from api import routes
