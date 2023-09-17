#!/usr/bin/python3
"""
102-relationship_cities_states_list module

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

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
