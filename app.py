from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template

import config
from base import Base
from request import Request
from sqlalchemy import create_engine

engine = create_engine(f'sqlite:////{config.DB_PATH}', echo=True)
Base.metadata.create_all(engine)

SessionFactory = sessionmaker(bind=engine)

app = Flask(__name__)

@app.route("/")
def main():
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

    return 'ok'