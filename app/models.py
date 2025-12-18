from app import db 
from datetime import datetime, timezone
 
class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(64), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
 
    def to_dict(self): 
        return { 
            'id': self.id, 
            'username': self.username, 
            'email': self.email, 
            'created_at': self.created_at.isoformat() if self.created_at else None 
        } 
