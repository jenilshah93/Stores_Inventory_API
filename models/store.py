from db import dba
class StoreModel(dba.Model):
    __tablename__ = 'stores'
    # __table_args__ = {'extend_existing': True}

    id = dba.Column(dba.Integer, primary_key=True)
    name = dba.Column(dba.String(80))

    items = dba.relationship('ItemModel',lazy = 'dynamic')

    def __init__(self,name):
        self.name = name


    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()


    def save_to_db(self):
        dba.session.add(self)
        dba.session.commit()



    def delete_from_db(self):
        dba.session.delete(self)
        dba.session.commit()
