from app.extension import SQL_DB


class Html(SQL_DB.Model):
    id = SQL_DB.Column(SQL_DB.Integer, primary_key=True, autoincrement=True)
    task_id = SQL_DB.Column(SQL_DB.String(96))
    problem = SQL_DB.Column(SQL_DB.Boolean, default=True)
    content = SQL_DB.Column(SQL_DB.Text)

    def __repr__(self):
        return "<{} for Task-{}>".format(
            "Problem" if self.problem else "Feedback",
            self.task_id,
        )
