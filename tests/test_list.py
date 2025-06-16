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

class TestCandies:
    @pytest.mark.usefixtures("empty_candies")
    def test_count_candies(self, candies):

        for candy in candies:
            CandiesServise.add(candy)

        assert CandiesServise.count() == 3

    def test_list_candies(self, candies):
        
        added_ids = []

        for candy in candies:
            added_candy = CandiesServise.add(candy)
            added_ids.append(added_candy["id"])

        all_candies = CandiesServise.list()

        for added_candy in all_candies:
            matching_candy = next((c for c in candies if c.title == added_candy["title"] and 
                                c.state == added_candy["state"] and 
                                c.owner == added_candy["owner"]), None)      
            assert matching_candy is not None
        
