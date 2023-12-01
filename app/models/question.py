from sqlalchemy.exc import SQLAlchemyError

from app.extension import SQL_DB
from app.utils.exception import ValidationError


class Question(SQL_DB.Model):
    id = SQL_DB.Column(SQL_DB.Integer, primary_key=True, autoincrement=True)
    question = SQL_DB.Column(SQL_DB.String(100))
    instruction = SQL_DB.Column(SQL_DB.Text)
    # samples = SQL_DB.relationship('Sample', backref='question', lazy=True)

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

    def validate(self, raise_exception=False):
        errors = {}
        if not self.question:
            errors["question"] = "Question cannot be empty."
        if not self.instruction:
            errors["instruction"] = "Instruction cannot be empty."

        if raise_exception and errors:
            raise ValidationError(errors)

        return errors

    @classmethod
    def create(cls, question: str, instruction: str):
        html_item = cls(question=question, instruction=instruction)
        html_item.validate(raise_exception=True)
        try:
            SQL_DB.session.add(html_item)
            SQL_DB.session.commit()
        except SQLAlchemyError:
            SQL_DB.session.rollback()
            raise
        return html_item
