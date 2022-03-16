from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    url = db.Column(db.String(255), unique=True)
    original_price = db.Column(db.Float)
    newest_price = db.Column(db.Float)
    image_url = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<Item {}>'.format(self.username)