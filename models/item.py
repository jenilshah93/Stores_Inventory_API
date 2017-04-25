from db import dba
class ItemModel(dba.Model):
    __tablename__ = 'items'

    id = dba.Column(dba.Integer, primary_key=True)
    name = dba.Column(dba.String(80))
    price = dba.Column(dba.Float(precision = 2))

    store_id  = dba.Column(dba.Integer, dba.ForeignKey('stores.id'))
    store = dba.relationship('StoreModel')
    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()


    def save_to_db(self):
        dba.session.add(self)
        dba.session.commit()



    def delete_from_db(self):
        dba.session.delete(self)
        dba.session.commit()
