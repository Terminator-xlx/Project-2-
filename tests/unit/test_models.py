import pytest 
from app.models import User 
from datetime import datetime 
 
def test_user_creation(): 
    # Test user model creation 
    user = User(username='testuser', email='test@example.com') 
 
    assert user.username == 'testuser' 
    assert user.email == 'test@example.com' 
    assert user.id is None  # Not saved to DB yet 
 
def test_user_to_dict(): 
    # Test model to_dict conversion 
    user = User(username='testuser', email='test@example.com') 
    user.id = 1 
    user.created_at = datetime.now()  # Set date manually 
 
    result = user.to_dict() 
 
    assert result['id'] == 1 
    assert result['username'] == 'testuser' 
    assert result['email'] == 'test@example.com' 
    assert 'created_at' in result 
    assert isinstance(result['created_at'], str)  # ISO format string 
