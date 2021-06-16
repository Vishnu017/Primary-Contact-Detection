from datetime import datetime,timedelta


import random as r

from api import db
from api.models import Main_Table,Visitor_List,Blacklist,Shop_Details



# DROP TABLE "positive_list";
# DROP TABLE "blacklist";
# DROP TABLE "shops";
# DROP TABLE "visitor_list";
# DROP TABLE "shop_details";
# DROP TABLE "main_table";


lst=["Akshay Kumar",
"Amitabh Bachchan",
"Brad Pitt",
"Alexandra Daddario",
"Alia Bhat",
"Anushka Sharma",
"Billie Eilish",
"Dwayne Johnson",
"Hritik Roshan",
"Margot Robbie",
"Priyanka Chopra",
"Tom Cruise",
"Virat Kohli",
"Gopika","Karthi","Rijas"]


shops=[4004,5005,6006]
shop_name=["Bismi","Sweat Palace","Royals"]
loc=["Kochi","thrik","pal"]


# # for ele in lst:


# #     usr=Main_Table()
# #     db.session.add(usr)
# #     db.session.commit()


# def "tstflask@gmail.com":
    
#     ph_no = []
    
#     # the first number should be in the range of 6 to 9
#     ph_no.append(str(r.randint(6, 9)))
    
#     # the for loop is used to append the other 9 numbers.
#     # the other 9 numbers can be in the range of 0 to 9.
#     for i in range(1, 10):
#         ph_no.append(str(r.randint(0, 9)))
    
       

#     return ("").join(ph_no)




def get_timestamp():

    hr=r.randint(0,2)
    ds=r.randint(0,2)
    mn=r.randint(0,30)
    dt=datetime.utcnow()

    fut=dt+timedelta(hours = hr)+timedelta(days=ds)+timedelta(minutes=mn)

    return fut
    

#TO add to main Table
for i in range(len(lst)):
    usr=Main_Table(lst[i],"tstflask@gmail.com")
    db.session.add(usr)
    db.session.commit()



#to add Shops

for i in range(len(shops)):
    
    sp=Shop_Details(shops[i],shop_name[i],loc[i],"tstflask@gmail.com")
    db.session.add(sp)
    db.session.commit()


#TO add to Visitor List

for _ in range(20):
    id=r.randint(1,len(lst))
    sp_id=r.choice(shops)

    usr=Visitor_List(id,sp_id,get_timestamp())
    db.session.add(usr)
    db.session.commit()


# to add Blacklist


# for _ in range(2):
#     no=r.randint(1,21)
#     usr=Blacklist(no,get_timestamp())
#     db.session.add(usr)
#     db.session.commit()





