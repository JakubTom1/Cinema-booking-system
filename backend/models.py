import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))

from sqlalchemy import (
    Column, Integer, String, Date, Time, ForeignKey, Boolean,
    Numeric, DateTime
)
from sqlalchemy.orm import relationship, backref
from database import Base, metadata, engine


# USERS
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(15), index=True)
    last_name = Column(String(15), index=True)
    status = Column(Integer, index=True, default=2)  # 0-admin, 1-staff, 2-client
    login = Column(String(50), unique=True, index=True)
    password = Column(String(128))

    transactions = relationship("Transaction", back_populates="user")


# MOVIES
class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50), index=True)

    showings = relationship("Showing", back_populates="movie")


# PRICE LIST
class Pricelist(Base):
    __tablename__ = 'pricelist'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type = Column(String(15), unique=True)
    ticket_price = Column(Numeric(5, 2), index=True)

    tickets = relationship("Ticket", back_populates="pricelist")


# CALENDAR
class Calendar(Base):
    __tablename__ = 'calendar'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(DateTime, index=True)

    showings = relationship("Showing", back_populates="calendar")


# HALLS
class Hall(Base):
    __tablename__ = 'halls'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    hall_num = Column(Integer, index=True)
    seats_amount = Column(Integer, index=True)

    seats = relationship("Seat", back_populates="hall")
    showings = relationship("Showing", back_populates="hall")


# SEATS
class Seat(Base):
    __tablename__ = 'seats'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_halls = Column(Integer, ForeignKey('halls.id'))
    seat_num = Column(Integer, index=True)
    row = Column(Integer, index=True)

    hall = relationship("Hall", back_populates="seats")
    tickets = relationship("Ticket", back_populates="seat")


# SHOWINGS
class Showing(Base):
    __tablename__ = 'showings'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_movies = Column(Integer, ForeignKey('movies.id'))
    id_hall = Column(Integer, ForeignKey('halls.id'))
    id_date = Column(Integer, ForeignKey('calendar.id'))
    hour = Column(Time)

    movie = relationship("Movie", back_populates="showings")
    hall = relationship("Hall", back_populates="showings")
    calendar = relationship("Calendar", back_populates="showings")
    transactions = relationship("Transaction", back_populates="showing")


# TRANSACTIONS
class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_users = Column(Integer, ForeignKey('users.id'))
    id_showings = Column(Integer, ForeignKey('showings.id'))
    status = Column(String(15), index=True)
    date = Column(Date)
    created_at = Column(DateTime, index=True)

    user = relationship("User", back_populates="transactions")
    showing = relationship("Showing", back_populates="transactions")
    tickets = relationship("Ticket", back_populates="transaction")
    answers = relationship("Answer", back_populates="transaction")


# TICKETS
class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_transaction = Column(Integer, ForeignKey('transactions.id'))
    id_pricelist = Column(Integer, ForeignKey('pricelist.id'))
    id_seat = Column(Integer, ForeignKey('seats.id'))

    transaction = relationship("Transaction", back_populates="tickets")
    pricelist = relationship("Pricelist", back_populates="tickets")
    seat = relationship("Seat", back_populates="tickets")



# SURVEYS
class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(200), index=True)
    question1 = Column(String(100), index=True)
    question2 = Column(String(100), index=True)
    question3 = Column(String(100), index=True)
    question4 = Column(String(100), index=True)
    question5 = Column(String(100), index=True)
    question6 = Column(String(100), index=True)
    question7 = Column(String(100), index=True)
    question8 = Column(String(100), index=True)
    question9 = Column(String(100), index=True)
    question10 = Column(String(100), index=True)

    answers = relationship("Answer", back_populates="survey")



# ANSWERS
class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_transaction = Column(Integer, ForeignKey('transactions.id'))
    id_survey = Column(Integer, ForeignKey('surveys.id'))
    date = Column(Date)
    ans_q1 = Column(String(200), index=True)
    ans_q2 = Column(String(200), index=True)
    ans_q3 = Column(String(200), index=True)
    ans_q4 = Column(String(200), index=True)
    ans_q5 = Column(String(200), index=True)
    ans_q6 = Column(String(200), index=True)
    ans_q7 = Column(String(200), index=True)
    ans_q8 = Column(String(200), index=True)
    ans_q9 = Column(String(200), index=True)
    ans_q10 = Column(String(200), index=True)

    transaction = relationship("Transaction", back_populates="answers")
    survey = relationship("Survey", back_populates="answers")


Base.metadata.create_all(engine)
