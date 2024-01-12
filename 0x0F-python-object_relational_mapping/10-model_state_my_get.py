#!/usr/bin/python3
"""
listing all States objects from the database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy import asc
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    input = sys.argv[4]
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    ss = Session()
    states = ss.query(State).filter_by(name=input).first()
    for state in states:
        print("{}: {}".format(state.id, state.name))
