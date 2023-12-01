from app.extension import SQL_DB


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

    def validate(self):
        pass
