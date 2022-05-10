from sqlalchemy import Column, String, Boolean

# Represents a client's request for a place
from base import Base


class Request(Base):
    __tablename__ = 'requests'

    name = Column(String)  # The name of the client
    phone_number = Column(String)
    id = Column(String, primary_key=True)
    wanted_locations = Column(String)  # Service ID's, seperated by ','
    error = Column(String)  # The error, if error has indeed occured.
    found = Column(Boolean, default=False) # If true - this row can be deleted
