from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import ForeignKey

engine = create_engine('sqlite:///week8/sqlite3.db')
engine.connect()

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name: str, fullname: str, password: str):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname,
                                            self.password)


class LoveRGBColor(Base):
    __tablename__ = 'love_rgb_color'
    id = Column(Integer, primary_key=True)
    color = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, color: str, user_id: int):
        self.user_id = user_id
        self.color = color


class WorkInfo(Base):
    __tablename__ = 'work_info'
    id = Column(Integer, primary_key=True)
    work_company = Column(String)
    post = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __init__(self, work_company: str, post: str, user_id: int):
        self.work_company = work_company
        self.post = post
        self.user_id = user_id


# Создание таблицы
Base.metadata.create_all(engine)