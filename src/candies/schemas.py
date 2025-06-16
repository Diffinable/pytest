
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class CandySchema(BaseModel):
    id: Optional[int] = Field(default=None, description="ID of the candy, auto-incremented by DB")
    title: str = Field(default="конфета")
    state: str = Field(default="full")
    owner: str = Field(default="teacher")

    model_config = ConfigDict(from_attributes=True)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        
        for attr in ["title", "state", "owner"]:
            if getattr(self, attr) != getattr(other, attr):
                return False
            
        return True
    
    def to_dict_wo_id(self) -> dict:
        return self.model_dump(exclude={"id"})

    
