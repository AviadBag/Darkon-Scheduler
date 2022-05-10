from sqlalchemy.orm import sessionmaker

from base import Base
from request import Request
from sqlalchemy import create_engine

engine = create_engine('sqlite:////home/aviad/PycharmProjects/PlacesScheduler/data.sqlite3', echo=True)
Base.metadata.create_all(engine)

SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()

session.add(Request(name=input('Enter Name'), id=input('Enter ID'), phone_number=input('Enter phone number'), wanted_locations=input('Enter wanted locations, seperated by "," example - 2161')))

session.commit()