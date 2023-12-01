from abc import ABC, abstractmethod

from sqlalchemy.exc import SQLAlchemyError

from app.extension import SQL_DB


class AbstractModel(ABC):
    @abstractmethod
    def validate(self, raise_exception=True):
        pass


def create(cls, **kwargs):
    item = cls(**kwargs)
    item.validate(raise_exception=True)
    try:
        SQL_DB.session.add(item)
        SQL_DB.session.commit()
    except SQLAlchemyError:
        SQL_DB.session.rollback()
        raise
    return item


def delete(cls, **kwargs):
    html_item = cls.query.filter_by(**kwargs).first()

    if not html_item:
        return

    try:
        SQL_DB.session.delete(html_item)
        SQL_DB.session.commit()
    except SQLAlchemyError:
        SQL_DB.session.rollback()
        raise


def exists(cls, **kwargs) -> bool:
    return not not SQL_DB.session.query(
        cls.query.filter_by(**kwargs).exists()
    ).scalar()


__all__ = [
    'create',
    'delete',
    'exists',
]
