#!/usr/bin/python3
"""
    a python script that lists all State objects from
    the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine, collate
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2],
                                                        argv[3]),
            pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    if argv[4]:
        state = session.query(State)\
            .filter(collate(State.name, 'utf8mb4_bin') == argv[4])\
            .order_by(State.id).first()

        if (state):
            print(state.id)
        else:
            print("Not found")

    session.close()
