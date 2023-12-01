from sqlalchemy.exc import SQLAlchemyError

from app.extension import SQL_DB
from app.utils.exception import ValidationError


class Html(SQL_DB.Model):
    id = SQL_DB.Column(SQL_DB.Integer, primary_key=True, autoincrement=True)
    task_id = SQL_DB.Column(SQL_DB.String(96))
    problem = SQL_DB.Column(SQL_DB.Boolean, default=True)
    content = SQL_DB.Column(SQL_DB.Text)

    __table_args__ = (
        SQL_DB.Index('task_id', task_id),
        SQL_DB.Index('problem', problem),
        SQL_DB.UniqueConstraint('task_id', 'problem'),
    )

    def __repr__(self):
        return "<{} for Task-{}>".format(
            "Problem" if self.problem else "Feedback",
            self.task_id,
        )

    def validate(self, raise_exception=False):
        errors = {}
        if not self.task_id:
            errors["task_id"] = "Task ID cannot be empty."
        if not self.content:
            errors["content"] = "Content cannot be empty."

        if raise_exception and errors:
            raise ValidationError(errors)

        return errors

    @classmethod
    def create(cls, task_id, problem, content):
        html_item = cls(task_id=task_id, problem=problem, content=content)
        html_item.validate(raise_exception=True)
        try:
            SQL_DB.session.add(html_item)
            SQL_DB.session.commit()
        except SQLAlchemyError:
            SQL_DB.session.rollback()
            raise
        return html_item

    @classmethod
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

    @classmethod
    def exists(cls, **kwargs) -> bool:
        exists = SQL_DB.session.query(
            cls.query.filter_by(**kwargs).exists()
        ).scalar()
        return not not exists

