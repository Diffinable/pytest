import time
import psycopg2
import pytest
from src.candies.service import CandiesServise
from src.candies.schemas import CandySchema
from src.db import Base, engine
from src.config import settings


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    print(f"{settings.DB_NAME=}")
    assert settings.MODE == "TEST"
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=("chrome", "firefox")
    )
    parser.addoption(
        "--run-slow",
        default="true",
        choices=("true", "false")
    )

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.mark.skipif('config.getoption("--run-slow") == "false"')
def test_slow():
    time.sleep(3)

    
def test_slow3():
    time.sleep(2)

    
def test_slow2():
    time.sleep(1)

    
def test_slow1():
    time.sleep(1)


def test_fast():
    pass
    
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