from app.extension import SQL_DB


class Response(SQL_DB.Model):
    id = SQL_DB.Column(SQL_DB.Integer, primary_key=True, autoincrement=True)
    response = SQL_DB.Column(SQL_DB.Text)
    prompt = SQL_DB.Column(SQL_DB.Integer, SQL_DB.ForeignKey('prompt.id'))
