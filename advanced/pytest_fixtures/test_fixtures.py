# pytest Fixtures Demonstration

import pytest

# A simulated database class
class MyDB:
    def __init__(self):
        self.connection = "Connected to DB"
    def fetch_user(self, user_id):
        if user_id == 1:
            return {"name": "Alice", "role": "admin"}
        return None
    def close(self):
        self.connection = "Disconnected"

# Define a fixture to handle database setup and teardown
# The fixture name is passed directly as an argument to test functions
@pytest.fixture
def db():
    # Setup
    my_db = MyDB()
    yield my_db  # provides the fixture object to the test cases
    # Teardown (runs after the test completes!)
    my_db.close()

# Test cases using the fixture
def test_fetch_user_admin(db):
    user = db.fetch_user(1)
    assert user["name"] == "Alice"
    assert user["role"] == "admin"

def test_fetch_invalid_user(db):
    user = db.fetch_user(99)
    assert user is None
