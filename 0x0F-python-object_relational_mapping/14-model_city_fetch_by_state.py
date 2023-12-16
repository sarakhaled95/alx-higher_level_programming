#!/usr/bin/python3
"""
script that lists all cities objects from hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from model_city import City
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":

    temp = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(temp.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    cities = session.query(State.name, City.id, City.name).filter(State.id == City.state_id)
    for city in cities:
        print(city[0] + ": (" + str(city[1]) + ")" + city[2])
