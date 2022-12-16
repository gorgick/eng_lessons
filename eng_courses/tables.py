import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Word(Base):
    __tablename__ = 'words'
    id = sa.Column(sa.Integer, primary_key=True)
    word = sa.Column(sa.String)
    translation = sa.Column(sa.String)
    kind = sa.Column(sa.String)
    course_id = sa.Column(sa.Integer, sa.ForeignKey("courses.id"))
    course = relationship('Course', back_populates='words')


class Course(Base):
    __tablename__ = 'courses'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    date = sa.Column(sa.Date)
    words = relationship('Word', back_populates='course')
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.Text, unique=True)
    username = sa.Column(sa.Text, unique=True)
    password_hash = sa.Column(sa.Text)

