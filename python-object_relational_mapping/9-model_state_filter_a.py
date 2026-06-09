#!/usr/bin/python3
"""Lists all State objects containing the letter 'a' from a MySQL database."""
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
        states = session.query(State).filter(
            State.name.contains('a')
        ).order_by(State.id).all()
        for state in states:
            print("{}: {}".format(state.id, state.name))
