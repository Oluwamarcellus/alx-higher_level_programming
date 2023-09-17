#!/usr/bin/python3
"""
101-relationship_states_cities_list module

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base
from sys import argv


if __name__ == "__main__":
    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()

    i = 1
    for idx, state in enumerate(states, start=1):
        print("{}: {}".format(idx, state.name))
        for city in state.cities:
            print("\t", end="")
            print("{}: {}".format(i, city.name))
            i += 1
