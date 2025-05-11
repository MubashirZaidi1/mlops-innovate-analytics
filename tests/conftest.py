import pytest
import os
import sys

# Add the project root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(autouse=True)
def setup_test_environment():
    """Setup test environment variables and configurations"""
    # Set test environment
    os.environ['FLASK_ENV'] = 'testing'
    
    # You can add more setup here if needed
    yield
    
    # Cleanup after tests if needed
    pass 