#!/usr/bin/python3
"""
    a python script that lists all State objects from
    the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2],
                                                        argv[3]),
            pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State.name, City.id, City.name)\
        .join(State).order_by(City.id).all()

    for state_name, city_id, city_name in res:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()
