from sqlalchemy import delete, func, insert, select, update
from src.db import Session
from src.candies.models import Candies


class CandiesRepository:
    @classmethod # написать для него тест
    def add(cls, values: dict):
        with Session() as session:
            stmt = insert(Candies).values(**values).returning(Candies)
            new_candy = session.execute(stmt)
            session.commit()
            return new_candy.scalar_one() 
        
    @classmethod    
    def get(cls, candy_id: int):
        with Session() as session:
            query = select(Candies.__table__.columns).filter_by(id=candy_id)
            candy = session.execute(query)
            return candy.mappings().one()
        
    @classmethod
    def list(cls, filter_by: dict):
        with Session() as session:
            query = select(Candies).filter_by(**filter_by)
            candies = session.execute(query)
            return candies.scalars().all()
        
    @classmethod
    def count(cls) -> int:
        with Session() as session:
            query = select(func.count(Candies.id)).select_from(Candies)
            candies_count = session.execute(query)
            return candies_count.scalar()
        
    @classmethod
    def update(cls, candy_id: int, values: dict):
        with Session() as session:
            stmt = update(Candies).where(Candies.id == candy_id).values(**values)
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete(cls, candy_id: int):
        with Session() as session:
            stmt = delete(Candies).where(Candies.id == candy_id)
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete_all(cls):
        with Session() as session:
            stmt = delete(Candies)
            session.execute(stmt)
            session.commit()