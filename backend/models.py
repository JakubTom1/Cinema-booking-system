import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))


from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, Boolean, Numeric, DateTime
from sqlalchemy.orm import relationship, backref
from database import Base, metadata, engine


# Model of Clients
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(15), index=True)
    last_name = Column(String(15), index=True)
    status = Column(Integer, index=True, default=2) # client(2), cinema staff(1) or admin(0)
    login = Column(String(50), unique=True, index=True)
    password = Column(String(128))

    transactions = relationship("Transaction", backref=backref("user"))

# Model of Movies
class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tittle = Column(String(50), index=True)


# Model of Price List
class Pricelist(Base):
    __tablename__ = 'pricelist'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type = Column(String(15), unique=True)
    ticket_price = Column(Numeric(5,2), index=True)

    tickets = relationship("Ticket", backref=backref("pricelist"))

class Calendar(Base):
    __tablename__ = 'calendar'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(DateTime, index=True)


# Model of Screening room
class Hall(Base):
    __tablename__ = 'halls'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    hall_num = Column(Integer, index=True)
    seats_amount = Column(Integer, index=True)

    seats = relationship("Seat", backref=backref("hall"))


# Model of Places
class Seat(Base):
    __tablename__ = 'seats'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_halls = Column(Integer, ForeignKey('halls.id'))
    seat_num = Column(Integer, index=True)
    row = Column(Integer, index=True)

    tickets = relationship("Ticket", backref=backref("seat"))



Base.metadata.create_all(engine)
