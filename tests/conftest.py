import psycopg2
import pytest
from src.candies.service import CandiesServise
from src.candies.schemas import CandySchema
from src.db import Base, engine



# @pytest.fixture(scope='session', autouse=True)
# def setup_database():
#     conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port="5432")
#     conn.autocommit = True
#     cur = conn.cursor()
#     cur.execute("DROP DATABASE IF EXISTS candies_test WITH (FORCE);")
#     cur.execute("CREATE DATABASE candies_test;")
#     cur.close()
#     conn.close()

#     from sqlalchemy import create_engine
#     test_engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/candies_test")
#     Base.metadata.create_all(test_engine)






@pytest.fixture
def faker_session_locale():
    return ['ru_RU']