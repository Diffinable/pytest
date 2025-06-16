import pytest
from src.candies.schemas import CandySchema
from src.candies.service import CandiesServise


    

@pytest.fixture
def candies():
    candies = [
        CandySchema(title="candy1", owner="Даниил"),
        CandySchema(title="candy2", state="eaten"),         
        CandySchema(title="candy3", state="half"),         
    ]
    return candies

@pytest.fixture
def empty_candies():
    CandiesServise.delete_all()