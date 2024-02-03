from sqlalchemy  import Column, Integer, VARCHAR
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Accounts(Base):

    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(length=50))
    password = Column(VARCHAR(length=50))
    age = Column(Integer)
    gender = Column(VARCHAR(length=25))

