from datetime import datetime
from enum import unique
from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///db.sqlite")
Session = sessionmaker(bind=engine)
session = Session()


class Sites(Base):
    __tablename__ = "sites"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), unique=True, nullable=False)
    url = Column(String(255), unique=True, nullable=False)
    keywords = Column(String(5000), nullable=False)
    cities = Column(String(1000), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


def create_record(site):
    session.add(site)
    session.commit()
    print(site)


Base.metadata.create_all(engine)


if __name__ == "__main__":
    pass