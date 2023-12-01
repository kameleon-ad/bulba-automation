from app.extension import SQL_DB
from app.utils.exception import ValidationError


class Html(SQL_DB.Model):
    id = SQL_DB.Column(SQL_DB.Integer, primary_key=True, autoincrement=True)
    task_id = SQL_DB.Column(SQL_DB.String(96))
    problem = SQL_DB.Column(SQL_DB.Boolean, default=True)
    content = SQL_DB.Column(SQL_DB.Text)

    __table_args__ = (
        SQL_DB.Index('task_id', task_id),
        SQL_DB.Index('problem', problem),
        SQL_DB.UniqueConstraint('task_id', 'problem'),
    )

    def __repr__(self):
        return "<{} for Task-{}>".format(
            "Problem" if self.problem else "Feedback",
            self.task_id,
        )

    def to_dict(self):
        return {
            "id": self.id,
            "task_id": self.task_id,
            "problem": self.problem,
            "content": self.content,
        }

    def validate(self, raise_exception=False):
        errors = {}
        if not self.task_id:
            errors["task_id"] = "Task ID cannot be empty."
        if not self.content:
            errors["content"] = "Content cannot be empty."

        if raise_exception and errors:
            raise ValidationError(errors)

        return errors
