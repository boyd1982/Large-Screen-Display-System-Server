# coding=utf-8
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class p_expert(db.Model):
    Id=db.Column(db.String(11), primary_key=True)
    Classification=db.Column(db.String(255))
    Field=db.Column(db.String(255))
    Name=db.Column(db.String(255))
    Sex=db.Column(db.String(255))
    Birthday=db.Column(db.String(255))
    Education=db.Column(db.String(255))
    Level=db.Column(db.String(255))
    Working_seniority=db.Column(db.Numeric)
    Phone=db.Column(db.String(255))
    City=db.Column(db.String(255))

class p_repair(db.Model):
    Id=db.Column(db.String(11), primary_key=True)
    Dep_name=db.Column(db.String(255))
    Per_name=db.Column(db.String(255))
    Major=db.Column(db.String(255))
    Post=db.Column(db.String(255))
    Office_num=db.Column(db.String(255))
    Phone=db.Column(db.String(255))
    City=db.Column(db.String(255))

class p_manager(db.Model):
    Id=db.Column(db.String(11), primary_key=True)
    Name=db.Column(db.String(255))
    Post=db.Column(db.String(255))
    Birthday=db.Column(db.String(255))
    Education=db.Column(db.String(255))
    Department=db.Column(db.String(255))
    Major=db.Column(db.String(255))
    Phone=db.Column(db.String(255))
    Health=db.Column(db.String(255))
    City=db.Column(db.String(255))

