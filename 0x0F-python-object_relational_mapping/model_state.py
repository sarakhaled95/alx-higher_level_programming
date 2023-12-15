#!/usr/bin/python3
"""model state that define state class"""

from sqlalchemy import Column, Integer, String, Metadata
from sqlalchemy.ext.declarative import declarative_base


myMetadata = Metadata()
Base = declarative_base(metadata=myMetadata)


class State(Base):
    """
    class with state attribute
    """

    __tablename__ = 'state'
    id = column(Integer, unique=True, nullable=False, primary_key=True)
    name = column(String(128), nullable=False)
