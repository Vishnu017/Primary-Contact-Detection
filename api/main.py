from flask import Blueprint, render_template,request,redirect,url_for,flash
from flask_login import login_required, current_user





from .extra_function import  csv_reader,send_mail
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
        print(x.filename)
        print(x)
        
        print(type(x.filename))
        print(x.content_type)
        if x.filename!="" and x.filename.rsplit('.', 1)[1].lower()=='csv':
            print("enter")
            y=x.read().decode()
            print(y)
            print("file over")
            with open("file.txt",'w',newline='') as f:
                f.write(y)
            print(f)
            mail_lst=csv_reader("file.txt")
            if mail_lst=="error":
                flash('Please check your csv file .')
                return render_template('profile.html', name=current_user.name)


            print(mail_lst)
            send_mail(mail_lst)
            return render_template('sumbit.html', name=current_user.name)



        
        # print(data)
        # print(x.mimetype)
        # if x == None:

        #     return "no file"

        # elif 'text/csv' != x.mimetype:
        
        #     return "not Csv"
        else:
            flash('Please upload a csv file .')
            return render_template('profile.html', name=current_user.name)


         

        

