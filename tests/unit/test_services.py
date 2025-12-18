import pytest 
from app.models import User 
 
def test_create_user_manually(app): 

    with app.app_context(): 
        from app import db 

        db.create_all() 
 
        user = User(username='manualuser', email='manual@test.com') 
        db.session.add(user) 
        db.session.commit() 
 
        assert user.id is not None 
        assert user.username == 'manualuser' 
        print(f'User created with id: {user.id}') 
