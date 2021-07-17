from flask import render_template,redirect,url_for,request,jsonify
from flask_mail import Mail, Message
from PIL import Image
from io import BytesIO
import  base64


from api import db
from api import app
from api import mail
from api.models import Main_Table,Visitor_List,Blacklist
from api.extra_function import *
from api.recognitionFromPhoto import Face_recog_function





@app.route('/Home',methods=["POST","GET"])

def home():

    # return f"{id}{sid}"
    if request.method=="GET":
        name=request.args.get('name')
        if name!=None:
            pid=Main_Table.query.filter(Main_Table.person_name==name).first().id
            return is_blacklist(pid,request.args.get('shop_id')  )
        return render_template('home.html')


    if request.method=="POST":


        name = request.args.get("id")
        shop_id = request.args.get("shop_id")
        print(shop_id)
        print(name)
        id=get_id(name)
        print(id)
        return is_blacklist(id,shop_id)



# @app.route('/Health_Official',methods=["POST","GET"])
# def hello_name():


#     if request.method=="GET":
#         return render_template("health.html")




#     if request.method=="POST":

#         lst = request.form.get("name[]")
#         ans=[]
#         for ele in lst:
#             ans.append(is_blacklist(ele,1001))


#         return ans



@app.route('/Face_recog',methods=["POST","GET"])
def Get_faceid():
    # shp_id=request.args.get("shop_id")
    # print(shp_id)
    name=Face_recog_function()
    if name=="Unknown":
        return name
    pid=name.split("_")[0]
    name=name.split("_")[1]
    print(pid)
    
    print(name)
    # return redirect(url_for("home",pid=pid,sid=shp_id),code=307)
    return name


    



# @app.route('/sent_mail',methods=["POST","GET"])

# def send_mail():
    
#     usrs=request.args.getlist('usrs')
#     print("Inside Send Mail")
#     sent_people=[]
#     print(type(usrs))
#     with mail.connect() as conn:
#         for usr in usrs:
#             print(usr)
#             person=Main_Table.query.filter(Main_Table.id==usr).first()
#             print(person.email)
#             print(type(person.email))
#             print(person.person_name)

#             if person.id not in sent_people:
#                 msg = Message('Primary Contact', sender = 'tstflask@gmail.com', recipients = [person.email])
#                 msg.body = f"""Dear {person.person_name},\nYou are a primary contact.Please stay inside your homes and follow the instructions provided by the health officials.\nFor further information contact\nhttps://www.mohfw.gov.in/ """
                
#                 conn.send(msg)
#                 sent_people.append(person.id)

#     print(sent_people)
#     return "Sent"



# @app.route('/postjson', methods = ['POST','GET'])
# def postJsonHandler():
#     if request.method=="POST":
#         print (request.is_json)
#         content = request.get_json()
#         print (content)
#         lst=[]
#         for ele in content['id']:
#             lst.append((ele['id'],ele['name']))
#         print(lst)
#         mail_lst=HealthAdd(lst)
#         print("mail_lst before redirecting")

#         print(mail_lst)
#         return redirect(url_for("send_mail",usrs=mail_lst))    



@app.route('/uploadPhoto', methods=['POST','GET'])
def uploadphoto():
    if request.method=="GET":
        return jsonify({'queerks' : quarks})

    else:
        img = request.get_json()
        # sh_id=img['sid']
        #Decoding the image
        im = Image.open(BytesIO(base64.b64decode(img['id'])))
        im.save('api/image.png', 'PNG')
        return redirect(url_for("Get_faceid"))
        

@app.route('/uploadData', methods=['POST','GET'])
def update():
    if request.method=="GET":
        pass
    else:
        person = request.get_json()
        name=person['name']
        sid=person["sid"]
        print(person,name)
        return redirect(url_for("home",shop_id=sid,name=name))
        