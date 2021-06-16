from flask import Blueprint, render_template,request,redirect,url_for
from flask_login import login_required, current_user


import pandas as pd
from io import StringIO

from .extra_function import  csv_reader
from . import routes

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    if request.method=='GET':
        return render_template('profile.html', name=current_user.name)

    if request.method=="POST":
        x=request.files["csv_file"]
        y=x.read().decode()
        with open("file.txt",'w',newline='',) as f:
            f.write(y)
        
        mail_lst=csv_reader("file.txt")
        
        # print(data)
        # print(x.mimetype)
        # if x == None:

        #     return "no file"

        # elif 'text/csv' != x.mimetype:
        
        #     return "not Csv"



        return redirect(url_for("send_mail",usrs=mail_lst)) 

        return "done"

