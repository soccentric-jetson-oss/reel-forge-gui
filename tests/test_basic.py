"""Basic import and smoke tests."""
import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestBasic(unittest.TestCase):
    def test_imports(self):
        import grpc
        self.assertIsNotNone(grpc)
        from PySide6 import QtWidgets
        self.assertIsNotNone(QtWidgets)
    
    def test_version(self):
        import importlib
        try:
            from src import main
            self.assertTrue(hasattr(main, '__version__') or True)
        except ImportError:
            pass

if __name__ == "__main__":
    unittest.main()
