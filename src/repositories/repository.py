from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update, delete

from src.db.db import session_maker


class AbstractRepository(ABC):
    @abstractmethod
    def add_one(self):
        raise NotImplementedError

    @abstractmethod
    def find_all(self):
        raise NotImplementedError

    @abstractmethod
    def find_one(self, **filter_by):
        raise NotImplementedError

    @abstractmethod
    def find_all_by_filter(self, **filter_by):
        raise NotImplementedError

    @abstractmethod
    def find_one(self, **filter_by):
        raise NotImplementedError

    @abstractmethod
    def edit_one(self, id: int, data: dict):
        raise NotImplementedError

    @abstractmethod
    def delete_one(self, **filter_by):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def add_one(self, data: dict):
        with session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = session.execute(stmt).scalar_one()
            session.commit()
            return res

    def find_all(self) -> list:
        with session_maker() as session:
            stmt = select(self.model)
            res = session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res

    def find_one(self, **filter_by):
        with session_maker() as session:
            stmt = select(self.model).filter_by(**filter_by)
            res = session.execute(stmt)
            res = res.scalar_one().to_read_model()
            return res

    def find_all_by_filter(self, **filter_by):
        with session_maker() as session:
            stmt = select(self.model).filter_by(**filter_by)
            res = session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res

    def edit_one(self, id: int, data: dict):
        with session_maker() as session:
            stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model.id)
            res = session.execute(stmt).scalar_one()
            session.commit()
            return res

    def delete_one(self, **filter_by):
        with session_maker() as session:
            stmt = delete(self.model).filter_by(**filter_by).returning(self.model.id)
            res = session.execute(stmt).scalar_one()
            session.commit()
            return res
