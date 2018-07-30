# coding: utf-8
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Attachment(Base):
    __tablename__ = 'attachment'

    id = Column(Integer, primary_key=True)
    attachment_id = Column(Integer, nullable=False)
    message_id = Column(Text, nullable=False)
    file_name = Column(Text, nullable=False)
    display_name = Column(Text, nullable=False)
    type = Column(Text, nullable=False)
    size = Column(Integer, nullable=False)


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    message_id = Column(Text, nullable=False)
    timestamp = Column(Integer, nullable=False)
    subject = Column(Text, nullable=False)
    body = Column(Text)
    html_body = Column(Text)
    _from = Column('from', Text, nullable=False)
    parsable = Column(Integer)
