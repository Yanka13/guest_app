from app import database


class Guest(database.Model):
    """Simple database model to track event attendees."""

    __tablename__ = 'guests'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(80))
    email = database.Column(database.String(120))
    group_size = database.Column(database.Integer, default=1)

    def __init__(self, name=None, email=None, group_size=1):
        self.name = name
        self.email = email
        self.group_size = group_size
