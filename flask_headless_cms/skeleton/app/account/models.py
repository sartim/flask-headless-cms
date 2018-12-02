from sqlalchemy.dialects.postgresql import UUID

from app import db


class AccountUser(db.Model):
	__tablename__ = 'account_users'

	id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True)
	name = db.Column(db.String(255))
	password = db.Column(db.String(255))
	phone_number = db.Column(db.String(255))
	is_active = db.Column(db.Boolean, default=False)

	def __repr__(self):
		return "%s(%s)" % (self.__class__.__name__, self.name)

	def __init__(self, name):
		self.id = id