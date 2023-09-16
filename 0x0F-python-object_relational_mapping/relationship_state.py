#!/usr/bin/python3
"""
relationship_state module

"""
from sqlalchemy import Column, Integer, MetaData, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Inherits the Base class and creates the state table in the DB
    """

    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
