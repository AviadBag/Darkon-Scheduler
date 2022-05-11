from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, request, redirect, url_for

import config
from base import Base
from request import Request
from sqlalchemy import create_engine

engine = create_engine(f'sqlite:////{config.DB_PATH}', echo=True)
Base.metadata.create_all(engine)

SessionFactory = sessionmaker(bind=engine)

app = Flask(__name__)

@app.route("/")
def index():
    # Retrieve data from db
    session = SessionFactory()
    all_requests = session.query(Request)

    # Render data
    return render_template('app.html', requests=all_requests)

@app.route('/delete/<id>')
def delete(id):
    session = SessionFactory()
    session.query(Request).filter_by(id=id).delete()
    session.commit()

    return ''

@app.route('/add')
def add():
    session = SessionFactory()

    name = request.args['name']
    id   = request.args['id']
    phone = request.args['phone']
    wanted_locations = []
    for key in request.args.keys():
        if key.isdigit(): # This is a service id
           wanted_locations.append(key)
    r = Request(name=name, id=id, phone_number=phone, wanted_locations=','.join(wanted_locations))
    session.add(r)
    session.commit()

    return redirect(url_for('index'))