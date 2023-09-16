#!/usr/bin/python3
"""
14-model_city_fetch_by_state module

"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    conn = "mysql://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    city = session.query(State, City).join(City).order_by(City.id)
    for state, city in city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
