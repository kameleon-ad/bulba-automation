from app.extension import SQL_DB
from app.utils.db import NoneNullColumn
from app.utils.exception import ValidationError


class Prompt(SQL_DB.Model):
    id = NoneNullColumn(SQL_DB.Integer, primary_key=True, autoincrement=True)
    prompt = NoneNullColumn(SQL_DB.Text)

    __table_args__ = (
        SQL_DB.Index('prompt_index', prompt),
        SQL_DB.UniqueConstraint('prompt'),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "prompt": self.prompt,
        }

    def validate(self, raise_exception: bool = False):
        errors = {}
        if not self.prompt:
            errors["prompt"] = "Question cannot be empty."

        if raise_exception and errors:
            raise ValidationError(errors)

        return errors
