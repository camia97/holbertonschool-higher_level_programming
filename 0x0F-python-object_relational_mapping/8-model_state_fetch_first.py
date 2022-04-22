#!/usr/bin/python3
"""All states via SQLAlchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://\
{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()
    r = session.query(State).order_by(State.id).first()
    if r is None:
        print('Nothing')
    else:
        print(f'{r.id}: {r.name}')
    session.close()
