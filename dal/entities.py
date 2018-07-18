# coding: utf-8
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AttachmentTable(Base):
    __tablename__ = 'attachment_table'

    id = Column(Integer, primary_key=True)
    attachmentId = Column(Integer, nullable=False)
    messageId = Column(Text, nullable=False)
    fileName = Column(Text, nullable=False)
    displayName = Column(Text, nullable=False)
    type = Column(Text, nullable=False)
    size = Column(Integer, nullable=False)
    savedLocation = Column(Text, nullable=False)


class MessageTable(Base):
    __tablename__ = 'message_table'

    id = Column(Integer, primary_key=True)
    messageId = Column(Integer, nullable=False)
    subject = Column(Text, nullable=False)
    _from = Column('from', Text, nullable=False)
    saveLocation = Column(Text, nullable=False)
