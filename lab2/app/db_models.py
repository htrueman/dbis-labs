import os

import sqlalchemy as sa
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ['DATABASE_URL'])
Base = declarative_base(engine)
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'

    full_name = sa.Column(sa.Unicode(250), nullable=False)
    type = sa.Column(sa.Unicode(20), nullable=False)
    date_registered = sa.Column(sa.Date(), nullable=False)
    user_id = sa.Column(sa.BigInteger, autoincrement=True, primary_key=True)
    group_name = sa.Column(sa.Unicode(6), ForeignKey('groups.name'), nullable=False)


class Group(Base):
    __tablename__ = 'groups'

    name = sa.Column(sa.Unicode(6), primary_key=True)


class LecturePack(Base):
    __tablename__ = 'lecture_packs'

    pack_name = sa.Column(sa.Unicode(150), primary_key=True)
    description = sa.Column(sa.Unicode(150), nullable=False)


class Lecture(Base):
    __tablename__ = 'lectures'

    text = sa.Column(sa.String, nullable=False)
    version = sa.Column(sa.Integer, nullable=True)
    created = sa.Column(sa.DateTime(), nullable=False)
    modified = sa.Column(sa.DateTime(), nullable=True)
    pack_name = sa.Column(sa.Unicode(250), ForeignKey('lecture_packs.pack_name'), nullable=True)
    lecture_id = sa.Column(sa.BigInteger, autoincrement=True, primary_key=True)
    prev_lecture_id = sa.Column(sa.BigInteger, ForeignKey('lectures.lecture_id'), nullable=True)
