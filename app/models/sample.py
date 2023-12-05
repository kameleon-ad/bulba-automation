from app.extension import SQL_DB
from app.utils.db import NoneNullColumn


class Sample(SQL_DB.Model):
    id = NoneNullColumn(SQL_DB.Integer, primary_key=True, autoincrement=True)
    prompt = NoneNullColumn(SQL_DB.Text)
    response = NoneNullColumn(SQL_DB.Text)
    question_id = NoneNullColumn(SQL_DB.Integer, SQL_DB.ForeignKey('question.id'))
    reason = NoneNullColumn(SQL_DB.Text)
    answer = NoneNullColumn(SQL_DB.String(32))

    question = SQL_DB.relationship('Question', foreign_keys=[question_id])

    def to_dict(self):
        return {
            "id": self.id,
            "prompt": self.prompt,
            "response": self.response,
            "question": self.question.question,
            "reason": self.reason,
            "answer": self.answer,
        }
