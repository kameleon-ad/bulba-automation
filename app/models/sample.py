from app.extension import SQL_DB


class Sample(SQL_DB.Model):
    id = SQL_DB.Column(SQL_DB.Integer, primary_key=True, autoincrement=True)
    question = SQL_DB.Column(SQL_DB.Integer, SQL_DB.ForeignKey('question.id'))
    prompt = SQL_DB.Column(SQL_DB.Integer, SQL_DB.ForeignKey('prompt.id'))
    answer = SQL_DB.Column(SQL_DB.String(32))
