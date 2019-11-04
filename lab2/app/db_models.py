import os

import sqlalchemy as sa
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

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
    group_id = sa.Column(sa.Unicode(6), ForeignKey('groups.group_id'), nullable=False)


class Group(Base):
    __tablename__ = 'groups'

    group_id = sa.Column(sa.BigInteger, autoincrement=True, primary_key=True)
    name = sa.Column(sa.Unicode(6), nullable=False)


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


class LectureActivity(Base):
    __tablename__ = 'lecture_activity'

    view_count = sa.Column(sa.Integer, nullable=False, default=0)
    like_count = sa.Column(sa.Integer, nullable=False, default=0)
    comment_count = sa.Column(sa.Integer, nullable=False, default=0)
    grade = sa.Column(sa.Integer, nullable=False, default=0)
    student_id = sa.Column(sa.BigInteger, ForeignKey('users.user_id'), nullable=False)
    lecture_id = sa.Column(sa.BigInteger, ForeignKey('lectures.lecture_id'), nullable=False)
    lecture_activity_id = sa.Column(sa.BigInteger, autoincrement=True, primary_key=True)


class Subject(Base):
    __tablename__ = 'subjects'

    name = sa.Column(sa.Unicode(150), primary_key=True)
    teacher_id = sa.Column(sa.BigInteger, ForeignKey('users.user_id'), nullable=False)
    lecture_id = sa.Column(sa.BigInteger, ForeignKey('lectures.lecture_id'), nullable=False)


class UniversitySubject(Base):
    __tablename__ = 'university_subject'

    id = sa.Column(sa.BigInteger, autoincrement=True, primary_key=True)

    subject_name = sa.Column(sa.Unicode(250), ForeignKey('subjects.name'), nullable=False)
    lecture_id = sa.Column(sa.BigInteger, ForeignKey('universities.id'), nullable=False)


class University(Base):
    __tablename__ = 'universities'

    id = sa.Column(sa.BigInteger, autoincrement=True, primary_key=True)

    name = sa.Column(sa.Unicode(250), nullable=False)
    city = sa.Column(sa.Unicode(250), nullable=False)
    count_staff = sa.Column(sa.Integer, nullable=False)
    year = sa.Column(sa.Integer, nullable=False)

    subjects = relationship("Subject", secondary="university_subject")
