from dataclasses import dataclass
from typing import List
from dateutil import parser
import datetime
import logging
import coloredlogs

from sqlalchemy.orm import sessionmaker
from base import Base
from request import Request
from sqlalchemy import create_engine

from set_appointment import set_appointment
from dates import get_avialable_dates
import slots

engine = None

def init_db():
    global engine
    engine = create_engine('sqlite:////home/aviad/PycharmProjects/PlacesScheduler/data.sqlite3', echo=False)
    Base.metadata.create_all(engine)

@dataclass
class Place:
    service_id: int
    date: datetime
    time: int

def is_date_ok(date: datetime):
    #return date.month == 5 and date.day <= 24
    return True

# Finds a place in the given location. Returns None if nothing was found.
def find_place(locations: List[int]) -> None | Place:
    for service_id in locations:
        dates = get_avialable_dates(service_id)
        if dates is None:
            return None
        logging.info(f'{service_id} - {len(dates)} places')
        for d in dates:
            date_str = d['calendarDate']
            calendar_id = d['calendarId']
            date = parser.parse(date_str)
            if is_date_ok(date):
                places = slots.get_places(service_id, calendar_id)
                try:
                    places = places['Results']
                    return Place(service_id=service_id, date=date, time=places[0]['Time'])
                except:
                    continue # There were either not places found or an invalid response
    return None # There was nothing found

def proccess_request(request: Request):
    logging.info(f'Trying to find a place for "{request.name}"')
    place = find_place(request.wanted_locations.split(','))
    if place is not None:
        logging.info(f'Found a good place for {request.name}')
        error = set_appointment(request.id, request.phone_number, place.service_id, place.date, place.time)
        if error == '': # We have got a place!
            logging.info(f'{request.name} has got a place, and can be deleted from the DB.')
            request.found = True
        else:
            logging.error(f'{request.name} - {error}')
            request.error = error

def init_logger():
    coloredlogs.install()
    logging.basicConfig(level=logging.INFO, format='(%(asctime)s) %(levelname)s -> %(message)s')

def main():
    init_logger()
    init_db()
    SessionFactory = sessionmaker(bind=engine)
    session = SessionFactory()

    # r = Request(id='327934741', name='aviad', phone_number='0556657219', wanted_locations='2161')
    # session.add(r)
    # session.commit()
    while True:
        all_requests = session.query(Request).filter_by(found=False)
        for r in all_requests:
            proccess_request(r)
        session.commit()



if __name__ == '__main__':
    main()