from app.extension import SQL_DB
from app.utils import ValidationError


class Sample(SQL_DB.Model):
    id = SQL_DB.Column(SQL_DB.Integer, primary_key=True, autoincrement=True)
    question = SQL_DB.Column(SQL_DB.Integer, SQL_DB.ForeignKey('question.id'))
    response = SQL_DB.Column(SQL_DB.Integer, SQL_DB.ForeignKey('response.id'))
    answer = SQL_DB.Column(SQL_DB.String(32))

    def to_dict(self):
        return {
            "id": self.id,
            "response": self.question,
            "prompt": self.response,
            "answer": self.answer,
        }

    def validate(self, raise_exception: bool = False):
        errors = {}
        if self.question is None:
            errors["question"] = "Question cannot be empty."
        if self.response is None:
            errors["response"] = "Response cannot be empty."
        if not self.answer:
            errors["answer"] = "Answer cannot be empty."

        if raise_exception and errors:
            raise ValidationError(errors)

        return errors
