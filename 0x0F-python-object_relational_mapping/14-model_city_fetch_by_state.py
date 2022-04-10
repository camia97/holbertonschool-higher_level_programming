#!/usr/bin/python3
"""All states via SQLAlchemy"""
from sqlalchemy import create_engine
from sqlalchemy import delete
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_city import Base, City
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://\
{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State)
    for j in session.query(State):
        for i in session.query(City).order_by(City.id):
            print(f'{j.name}: ({i.id}) {i.name}')
    session.close()
