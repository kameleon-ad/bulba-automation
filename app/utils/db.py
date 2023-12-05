from sqlalchemy import Column as BaseColumn
from sqlalchemy.exc import SQLAlchemyError

from app.extension import SQL_DB


class NoneNullColumn(BaseColumn):
    inherit_cache = False

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('nullable', False)
        super().__init__(*args, **kwargs)


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


def get_create(cls, **kwargs):
    item = cls.query.filter_by(**kwargs).first()
    if item:
        return item
    return create(cls, **kwargs)


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
    query = cls.query.filter_by(**kwargs).exists()
    result = SQL_DB.session.query(query)
    scalar = result.scalar()
    return not not scalar


__all__ = [
    'create',
    'get_create',
    'delete',
    'exists',
]
