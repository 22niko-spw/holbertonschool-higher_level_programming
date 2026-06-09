#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    state_name_search = sys.argv[4]

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (
        session.query(State)
        .filter(State.name == state_name_search)
        .first()
    )

    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
