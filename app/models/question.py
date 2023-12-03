from app.extension import SQL_DB
from app.utils.db import NoneNullColumn
from app.utils.exception import ValidationError


class Question(SQL_DB.Model):
    id = NoneNullColumn(SQL_DB.Integer, primary_key=True, autoincrement=True)
    question = NoneNullColumn(SQL_DB.String(128))
    instruction = NoneNullColumn(SQL_DB.Text)

    __table_args__ = (
        SQL_DB.Index('question_index', question),
        SQL_DB.UniqueConstraint('question'),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "instruction": self.instruction,
        }

    def validate(self, raise_exception: bool = False):
        errors = {}
        if not self.question:
            errors["question"] = "Question cannot be empty."
        if self.instruction is None :
            errors["instruction"] = "Instruction cannot be empty."

        if raise_exception and errors:
            raise ValidationError(errors)

        return errors
