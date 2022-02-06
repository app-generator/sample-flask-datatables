# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime
import json

from app import db

class Data(db.Model):

    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)

    code     = db.Column(db.String(64))   # product code 
    name     = db.Column(db.String(128))  # product name
    value    = db.Column(db.Integer)      # numeric
    currency = db.Column(db.String(10))   # string: usd, euro
    type     = db.Column(db.String(64))   # transaction
    ts       = db.Column(db.Integer, default=datetime.utcnow().timestamp())

    def __repr__(self):
        return self.toJSON()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update_value(self, new_value):
        self.value = new_value

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def toDICT(self):

        cls_dict          = {}
        cls_dict['ID']   = self.id
        cls_dict['Product Code'] = self.code
        cls_dict['Description'] = self.name
        cls_dict['Price'] = self.value
        cls_dict['Currency'] = self.currency
        cls_dict['TimeStamp'] = datetime.utcfromtimestamp(self.ts).strftime('%Y-%m-%d')

        return cls_dict

    def toJSON(self):

        return self.toDICT()
