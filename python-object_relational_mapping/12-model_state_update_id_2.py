#!/usr/bin/python3
"""Changes the name of the State with id=2 to 'New Mexico' in the database."""
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
        state = session.query(State).filter(State.id == 2).first()
        if state is not None:
            state.name = "New Mexico"
            session.commit()
