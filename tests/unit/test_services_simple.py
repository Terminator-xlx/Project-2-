import pytest 
from app.models import User 
 
def test_simple_user_creation(app): 
    with app.app_context(): 
        from app import db 
        user = User(username='simple', email='simple@test.com') 
        db.session.add(user) 
        db.session.commit() 
        assert user.id is not None 

