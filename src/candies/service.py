from typing import Optional
from pydantic import TypeAdapter
from src.candies.schemas import CandySchema
from src.candies.repository import CandiesRepository

class CandiesServise:
    @classmethod
    def add(cls, candy: CandySchema):
        candy_dict = candy.to_dict_wo_id()
        new_candy = CandiesRepository.add(candy_dict)
        return TypeAdapter(CandySchema).dump_python(new_candy)
    
    @classmethod
    def get(cls, candy_id: int):
        candy = CandiesRepository.get(candy_id)
        return TypeAdapter(CandySchema).dump_python(candy)
    
    @classmethod 
    def list(
        cls,
        title: Optional[str] = None,
        status: Optional[str] = None,
        owner: Optional[str] = None, 
    ):
        filter_by = {k: v for k, v in {"title": title, "status": status, "owner": owner}.items() if v}
        candies = CandiesRepository.list(filter_by)
        return TypeAdapter(list[CandySchema]).dump_python(candies)
    
    @classmethod
    def count(cls) -> int:
        count = CandiesRepository.count()
        return count

    @classmethod
    def update(cls, candy_id: int, candy: CandySchema):
        candy_dict = candy.to_dict_wo_id()
        CandiesRepository.update(candy_id, candy_dict)

    @classmethod
    def finish(cls, candy_id: int):
        CandiesRepository.update(candy_id, {"status": "eaten"})

    @classmethod
    def delete(cls, candy_id: int):
        CandiesRepository.delete(candy_id)

    @classmethod
    def delete_all(cls):
        CandiesRepository.delete_all()