from app import app
from db import dba

dba.init_app(app)

@app.before_first_request
def create_tables():
    dba.create_all()
