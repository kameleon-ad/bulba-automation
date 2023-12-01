from app.extension import SQL_DB
from app.utils import ValidationError
from app.utils.db import NoneNullColumn


class Answer(SQL_DB.Model):
    id = NoneNullColumn(SQL_DB.Integer, primary_key=True, autoincrement=True)
    answer = NoneNullColumn(SQL_DB.String(32))
    correct = NoneNullColumn(SQL_DB.Boolean, default=False)
    question_id = NoneNullColumn(SQL_DB.Integer, SQL_DB.ForeignKey('question.id'))
    response_id = NoneNullColumn(SQL_DB.Integer, SQL_DB.ForeignKey('response.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "answer": self.answer,
            "response_id": self.question_id,
            "prompt_id": self.response_id,
        }

    def validate(self, raise_exception: bool = False):
        errors = {}
        if not self.answer:
            errors["answer"] = "Answer cannot be empty."
        if self.question_id is None:
            errors["question_id"] = "Question cannot be empty."
        if self.response_id is None:
            errors["response_id"] = "Response cannot be empty."

        if raise_exception and errors:
            raise ValidationError(errors)

        return errors
