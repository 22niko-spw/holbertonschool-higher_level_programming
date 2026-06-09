#!/usr/bin/python3
"""Prints all City objects from a MySQL database with their state name."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    with Session(engine) as session:
        results = session.query(State, City).filter(
            State.id == City.state_id
        ).order_by(City.id).all()
        for state, city in results:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
