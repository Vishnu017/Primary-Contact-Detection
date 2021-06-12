from api import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#from sqlalchemy.dialects.postgresql import JSON


class Main_Table(db.Model):
    __tablename__ = 'main_table'

    id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String())
    email = db.Column(db.String(20))

    #backref creates a virtual column on the child class where it refers back to the parent.
    visitors = db.relationship('Visitor_List', backref='person')

    def __init__(self, person_name, email):
        self.person_name = person_name
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id)

#assosiation table for the many-to-many relationship between shop_details and visitor_list
shopvis = db.Table('shops',
            db.Column('shop', db.Integer, db.ForeignKey('visitor_list.id')),
            db.Column('id', db.Integer, db.ForeignKey('shop_details.shop'))
            )



class Shop_Details(db.Model):
    __tablename__ = 'shop_details'

    shop = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(20))
    shop_location = db.Column(db.String(20))
    manager_email = db.Column(db.String(20))

    #attribute to create the connection between shop_details and visitors_list
    shopvisitors = db.relationship('Visitor_List', secondary=shopvis, backref=db.backref('shoppers'), lazy=True)

    def __init__(self, shop, shop_name, shop_location, manager_email):
        self.shop_name = shop_name
        self.shop = shop
        self.shop_location = shop_location
        self.manager_email = manager_email

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Visitor_List(db.Model):
    __tablename__ = 'visitor_list'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer,db.ForeignKey('main_table.id'))
    shop_id = db.Column(db.Integer, db.ForeignKey('shop_details.shop'))
    time_stamp = db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self, *args):

        if len(args)==3:
            self.person_id = args[0]
            self.shop_id =  args[1]
            self.time_stamp =  args[2]

        elif len(args)==2:
            self.person_id = args[0]
            self.shop_id =  args[1]

        else:
            print("error")

    
    def __repr__(self):
        return '<id {}>'.format(self.person_id)



class Blacklist(db.Model):
    __tablename__ = 'blacklist'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('main_table.id'))
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)



    def __init__(self, *args):

        if len(args)==2:
            self.person_id = args[0]

            self.time_stamp =  args[1]

        elif len(args)==1:
            self.person_id = args[0]


        else:
            print("error")

    def __repr__(self):
        return '<id {}>'.format(self.person_id)





