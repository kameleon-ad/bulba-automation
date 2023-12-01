from app.extension import SQL_DB
from app.utils.exception import ValidationError


class Html(SQL_DB.Model):
    id = SQL_DB.Column(SQL_DB.Integer, primary_key=True, autoincrement=True)
    problem = SQL_DB.Column(SQL_DB.Boolean, default=True)
    content = SQL_DB.Column(SQL_DB.Text)
    mark = SQL_DB.Column(SQL_DB.Integer)

    # __table_args__ = (
    #     SQL_DB.Index('content_index', content),
    #     SQL_DB.UniqueConstraint('content', 'problem'),
    # )

    def __repr__(self):
        return "<The Html-{}: {}>".format(self.id, "Problem" if self.problem else "Feedback")

    def to_dict(self):
        return {
            "id": self.id,
            "problem": self.problem,
            "content": self.content,
            "mark": self.mark,
        }

    def validate(self, raise_exception: bool = False):
        errors = {}
        if self.problem is None:
            errors["problem"] = "This field cannot be None."
        if not self.content:
            errors["content"] = "Content cannot be empty."

        if raise_exception and errors:
            raise ValidationError(errors)

        return errors
