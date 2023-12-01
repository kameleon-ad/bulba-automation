from app.extension import SQL_DB
from app.utils.exception import ValidationError


class Question(SQL_DB.Model):
    id = SQL_DB.Column(SQL_DB.Integer, primary_key=True, autoincrement=True)
    question = SQL_DB.Column(SQL_DB.String(100))
    instruction = SQL_DB.Column(SQL_DB.Text)

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
        if not self.instruction:
            errors["instruction"] = "Instruction cannot be empty."

        if raise_exception and errors:
            raise ValidationError(errors)

        return errors
