# test_modelhelix.py
"""
Tests for ModelHelix module.
"""

import unittest
from modelhelix import ModelHelix

class TestModelHelix(unittest.TestCase):
    """Test cases for ModelHelix class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModelHelix()
        self.assertIsInstance(instance, ModelHelix)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModelHelix()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
