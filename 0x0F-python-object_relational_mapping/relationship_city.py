#!/usr/bin/python3
"""
relationship_city module

"""
from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base


class City(Base):
    """
    Inherits the Base class and creates the city table in the DB
    """

    __tablename__ = "cities"

    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
