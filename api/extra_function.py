from datetime import datetime,timedelta
import pytz    
import tzlocal 
import csv
from flask_mail import Message

from api.models import Main_Table,Visitor_List,Blacklist,Shop_Details
from api import db
from api import mail

def HealthAdd(lst):
    mail_lst=[]
    lst=[id for id,ele in lst]
    add_to_primary(lst)
    for ele in lst:
        tmp=get_time(ele)
        mail_lst.extend(tmp)

    print("exit HealthADd")
    return mail_lst
    







def get_name(id):

    user=Main_Table.query.get(id)
    return user.person_name





def get_id(name):



    user=Main_Table.query.filter_by(person_name=name).first()
    return user.id




def add_to_primary(lst):
    for usr in lst:


        check= Blacklist.query.filter(Blacklist.person_id==usr).first()
        if check:
            check.time_stamp=changetoist(datetime.utcnow())
            db.session.commit()
            continue
        usr=Blacklist(usr)
        db.session.add(usr)
        db.session.commit()
        





def short_list(fut,pas,id,s_id):
    print("Start ...entry")
    usrs=Visitor_List.query.filter((Visitor_List.person_id!=id)&(Visitor_List.shop_id==s_id ) & (Visitor_List.time_stamp>=pas ) & (Visitor_List.time_stamp<=fut)).all()
    print(usrs)
    if usrs==None:
        print("no entry")
    lst=[]
    for usr in usrs:
        if usr.person_id not in lst:
            lst.append(usr.person_id)
    print(lst)
    add_to_primary(lst)
    return lst


def get_time(id):
    usrs=Visitor_List.query.filter_by(person_id=id).all()
    mail_lst=[]
    for usr in usrs:
        dt=usr.time_stamp
        s_id=usr.shop_id
        fut=dt+timedelta(minutes = 30)
        pas=dt-timedelta(minutes = 30)
        print(fut,pas)
        tmp=short_list(fut,pas,id,s_id)
        print("tmp")
        print(tmp)

        mail_lst.extend(tmp)
    print("mail_lst")

    print(mail_lst,id)

    return mail_lst





def add_visitor(id,shop_id):

    usr=Visitor_List(id,shop_id)
    db.session.add(usr)
    db.session.commit()


def is_blacklist(id,shop_id):
    ans=Blacklist.query.filter_by(person_id=id).first()

    

    if ans == None:
    
        add_visitor(id,shop_id)
        return "True"
    send_mail_health(id,shop_id)
    return "False"



def csv_reader(x):
    lst=[]
    print()
    with open(x, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            lst.append(row)
    
    
    mail_lst=HealthAdd(lst)
    print("mail_lst before redirecting")

    print(mail_lst)
    return mail_lst





def changetoist(utc_time):
    local_timezone = tzlocal.get_localzone()
    #print(local_timezone)
    utc_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
    utc_time = utc_time.replace(tzinfo = None)
    return utc_time




def send_mail_health(usr,shid):
    

    rec="healthdepartment007@gmail.com"
    usr=get_name(usr)
    print("Inside Send HEalth Mail")
    sh_name=Shop_Details.query.filter(Shop_Details.shop==shid).first().shop_name
    print(sh_name)

    msg = Message('Violation', sender = 'tstflask@gmail.com', recipients = [rec])
    msg.body = f""" The following person {usr} has violated the protocols at {sh_name} on {changetoist(datetime.utcnow()).strftime("%Y-%m-%d %H:%M:%S")}."""
    
    mail.send(msg)
    

    print("sent to health")



def send_mail(lst):
    
    mail_lst=lst
    print("Inside Send Mail")
    sent_people=[]
    
    with mail.connect() as conn:
        for usr in mail_lst:
            print(usr)
            person=Main_Table.query.filter(Main_Table.id==usr).first()
            print(person.email)
            print(type(person.email))
            print(person.person_name)

            if person.id not in sent_people:
                msg = Message('Primary Contact', sender = 'tstflask@gmail.com', recipients = [person.email])
                msg.body = f"""Dear {person.person_name},\nYou are a primary contact.Please stay inside your homes and follow the instructions provided by the health officials.\nFor further information contact\nhttps://www.mohfw.gov.in/ """
                
                conn.send(msg)
                sent_people.append(person.id)

    print(sent_people)
    return "Sent"

    
