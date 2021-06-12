from datetime import datetime,timedelta


from api.models import Main_Table,Visitor_List,Blacklist
from api import db

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
            check.time_stamp=datetime.utcnow()
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
        return "Not positive ..added To Visitor Table"

    return ("Is positive")
