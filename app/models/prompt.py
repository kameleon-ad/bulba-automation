from sqlalchemy.exc import SQLAlchemyError

from app.extension import SQL_DB
from app.utils.exception import ValidationError


class Prompt(SQL_DB.Model):
    id = SQL_DB.Column(SQL_DB.Integer, primary_key=True, autoincrement=True)
    prompt = SQL_DB.Column(SQL_DB.String)
    # samples = SQL_DB.relationship('Sample', backref='prompt', lazy=True)

    __table_args__ = (
        SQL_DB.Index('prompt_index', prompt),
        SQL_DB.UniqueConstraint('prompt'),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "prompt": self.prompt,
        }

    def validate(self, raise_exception=False):
        errors = {}
        if not self.prompt:
            errors["prompt"] = "Question cannot be empty."

        if raise_exception and errors:
            raise ValidationError(errors)

        return errors

    @classmethod
    def create(cls, prompt: str):
        html_item = cls(prompt=prompt)
        html_item.validate(raise_exception=True)
        try:
            SQL_DB.session.add(html_item)
            SQL_DB.session.commit()
        except SQLAlchemyError:
            SQL_DB.session.rollback()
            raise
        return html_item
