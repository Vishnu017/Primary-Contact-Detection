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
    try:
        lst=[get_id(ele) for id,ele in lst]
        add_to_primary(lst,0)
        blacklst=Blacklist.query.all()
        print(blacklst)
        for ele in lst:
            tmp=get_time(ele,blacklst)
            mail_lst.extend(tmp)

        print("exit HealthADd")
        return mail_lst

    except Exception as e:
        print(e)
        return "error"
        







def get_name(id):

    user=Main_Table.query.get(id)
    return user.person_name





def get_id(name):



    user=Main_Table.query.filter_by(person_name=name).first()
    return user.id




def add_to_primary(lst,flag):
    if flag==0:
        for usr in lst:
            #Health people adding primary contacts

            check= Blacklist.query.filter(Blacklist.person_id==usr).first()
            if check:
                check.time_stamp=changetoist(datetime.utcnow())
                db.session.commit()
                continue
            usr=Blacklist(usr)
            db.session.add(usr)
            db.session.commit()
            
                


    if flag ==1:
        for usr in lst:
    
            #shortlist function  adding primary contacts

            check= Blacklist.query.filter(Blacklist.person_id==usr.person_id).first()
            
            if check == None:
                usr=Blacklist(usr.person_id,usr.time_stamp)
                db.session.add(usr)
                db.session.commit()

            else:
                if usr.time_stamp>check.time_stamp:
                    check.time_stamp=usr.time_stamp
                    db.session.commit()

                
            




def short_list(fut,pas,id,s_id,blacklst):
    # print("Start ...entry")
    blacklst=[usr.person_id for usr in blacklst]
    usrs=Visitor_List.query.filter((Visitor_List.person_id!=id)&(Visitor_List.shop_id==s_id ) & (Visitor_List.time_stamp>=pas ) & (Visitor_List.time_stamp<=fut)).all()
    
    if usrs==None:
        print("no entry")
    lst=[]
    for usr in usrs:
        if usr.person_id not in blacklst:
            lst.append(usr)
            print("add to primary lst")
            print(lst)
    
    add_to_primary(lst,1)
    return [usr.person_id for usr in lst]


def get_time(id,blacklst):
    usrs=Visitor_List.query.filter_by(person_id=id).all()
    mail_lst=[]
    for usr in usrs:
        dt=usr.time_stamp
        s_id=usr.shop_id
        fut=dt+timedelta(minutes = 30)
        pas=dt-timedelta(minutes = 30)
        # print(fut,pas)
        tmp=short_list(fut,pas,id,s_id,blacklst)
        # print("tmp")
        

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
            if row==[]:
                continue
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
    print("Inside Send Mail to primary contacts")
    sent_people=[]
    
    with mail.connect() as conn:
        for usr in mail_lst:
            
            person=Main_Table.query.filter(Main_Table.id==usr).first()
     

            if person.id not in sent_people:
                msg = Message('Primary Contact', sender = 'tstflask@gmail.com', recipients = [person.email])
                msg.body = f"""Dear {person.person_name},\nThis is a mail from the national health center.You have come into contact with a covid positive person in the last 14 days.\nHence you have been marked as a primary contact.Please stay inside your homes and follow the instructions provided by the health officials.\nFor further information contact\nhttps://www.mohfw.gov.in/ """
                
                conn.send(msg)
                sent_people.append(person.id)

    print(sent_people)
    return "Sent"

    
