from datetime import datetime
from config import db, ma

class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    desc = db.Column(db.String(300))
    image = db.Column(db.String(200))
    create_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class RoomSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Room
        load_instance = True
