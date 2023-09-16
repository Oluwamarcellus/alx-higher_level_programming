#!/usr/bin/python3
"""
12-model_state_update_id_2 module

"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    conn = "mysql://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.add(state)
        session.commit()
