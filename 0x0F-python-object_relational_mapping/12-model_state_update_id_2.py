#!/usr/bin/python3
"""
script that lists all state objects from hbtn_0e_6_usa
"""

if __name__ == "__main__":

    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    import sys

    temp = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(temp.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    states = session.query(State).filter_by(id=2).first()
    states.name = 'New Mexico'
    session.commit()
