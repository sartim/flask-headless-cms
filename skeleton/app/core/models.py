from ...app import app, db


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_date = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @staticmethod
    def create(obj):
        db.session.add(obj)
        obj.save()
        return obj

    @staticmethod
    def save():
        app.logger.debug("Successfully saved object")
        db.session.commit()