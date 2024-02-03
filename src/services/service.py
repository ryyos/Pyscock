import os

from faker import Faker
from random import randint, choice
from dotenv import load_dotenv
from icecream import ic

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy_cockroachdb import run_transaction

from src.model.accounts import Accounts
from src.exceptions.BadParamaterException import BadParamaterException

class Service:
    def __init__(self) -> None:
        load_dotenv()
        self.__database = os.getenv('DATABASE_URL').replace("postgresql://", "cockroachdb://")
        
        self.__faker = Faker()
        ...

    def create_account(self, session: Session, **kwargs) -> None:

        try:
            id = randint(1, 999999)
            username = kwargs["username"]
            password = kwargs["password"]
            age = kwargs["age"]
            gender = kwargs["gender"]

            ic(username)
            ic(age)
            ic(gender)

        except KeyError:
            raise KeyError()
        
        finally: 
            session.add(Accounts(id=id, username=username, password=password, age=age, gender=gender))
        ...

    def main(self) -> None:
        try: engine = create_engine(url=self.__database)
        except Exception as err: ic(err)

        for _ in range(100):
            run_transaction(sessionmaker(bind=engine),
                            lambda s: self.create_account(
                                session=s,
                                username=self.__faker.name(), 
                                password=self.__faker.password(),
                                age=randint(1, 70),
                                gender=choice(['male', 'female'])))
            
        
        ...

