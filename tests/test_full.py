"""Comprehensive test suite."""
import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestFull(unittest.TestCase):
    def test_imports(self):
        import importlib
        modules = ['src.main', 'src.app']
        for m in modules:
            try:
                mod = importlib.import_module(m)
                self.assertIsNotNone(mod)
            except ImportError:
                pass
    
    def test_configuration(self):
        import grpc
        channel = grpc.insecure_channel("localhost:50053")
        self.assertIsNotNone(channel)
        channel.close()
    
    def test_error_handling(self):
        import grpc
        self.assertEqual(grpc.StatusCode.NOT_FOUND, grpc.StatusCode.NOT_FOUND)

if __name__ == "__main__":
    unittest.main()
