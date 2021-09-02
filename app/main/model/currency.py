
from .. import db


class Currency(db.Model):
    """ Currency Model for storing user related details """
    __tablename__ = "currency"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.String(100), nullable=False)
    currency_from = db.Column(db.String(30), nullable=False)
    currency_to = db.Column(db.String(30), nullable=False)
    days = db.Column(db.JSON, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Currency '{}'>".format(self.amount)
