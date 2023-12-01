from app.extension import SQL_DB
from app.utils import ValidationError
from app.utils.db import NoneNullColumn


class Response(SQL_DB.Model):
    id = NoneNullColumn(SQL_DB.Integer, primary_key=True, autoincrement=True)
    response = NoneNullColumn(SQL_DB.Text)
    prompt_id = NoneNullColumn(SQL_DB.Integer, SQL_DB.ForeignKey('prompt.id'))

    prompt = SQL_DB.relationship('Prompt', foreign_keys=[prompt_id])

    def to_dict(self):
        return {
            "id": self.id,
            "response": self.response,
            "prompt": self.prompt.to_dict(),
        }

    def validate(self, raise_exception: bool = False):
        errors = {}
        if not self.response:
            errors["response"] = "Response cannot be empty."
        if self.prompt_id is None:
            errors["prompt_id"] = "Prompt cannot be empty."

        if raise_exception and errors:
            raise ValidationError(errors)

        return errors
