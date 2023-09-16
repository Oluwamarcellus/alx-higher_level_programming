#!/usr/bin/python3
"""
model_state module

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Inherits the Base class and creates the state table in the DB
    """

    __tablename__ = "states"

    id = Column(
            "id", Integer, nullable=False,
            primary_key=True, autoincrement=True
            )
    name = Column("name", String(128), nullable=False)
