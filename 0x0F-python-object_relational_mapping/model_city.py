#!/usr/bin/python3
"""
model_city module

"""
from sqlalchemy import Column, ForeignKey, Integer, String, null
from model_state import Base


class City(Base):
    """
    Inherits the Base class and creates the city table in the DB
    """

    __tablename__ = "cities"

    id = Column(
            "id", Integer, nullable=False,
            primary_key=True, autoincrement=True
            )
    name = Column("name", String(128), nullable=False)
    state_id = Column(
            "state_id", Integer, nullable=False,
            ForeignKey("states.id")
            )
