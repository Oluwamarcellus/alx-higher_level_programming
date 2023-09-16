#!/usr/bin/python3
"""
100-relationship_states_cities module

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base
from sys import argv


if __name__ == "__main__":
    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    session.add(new_state)
    session.commit()
    new_city = City(name='San Francisco', state=new_state)
    session.add(new_city)
    session.commit()
