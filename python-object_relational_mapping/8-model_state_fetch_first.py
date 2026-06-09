#!/usr/bin/python3
"""Prints the first State object from a MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )
    with Session(engine) as session:
        state = session.query(State).order_by(State.id).first()
        if state is None:
            print("Nothing")
        else:
            print("{}: {}".format(state.id, state.name))
