import pytest
from src.candies.schemas import CandySchema
from src.candies.service import CandiesServise

@pytest.fixture
def candies():
    candies = [
        CandySchema(title="candy1", owner="Даниил"),
        CandySchema(title="candy2", state="eaten"),         
    ]
    return candies

def test_count_candies(candies):
    CandiesServise.delete_all()

    for candy in candies:
        CandiesServise.add(candy)

    assert CandiesServise.count() == 2

def test_list_candies(candies):
    CandiesServise.delete_all()
    

    for candy in candies:
        CandiesServise.add(candy)
    all_candies = CandiesServise.list()

    for added_candy in all_candies:
        assert added_candy in candies
    
