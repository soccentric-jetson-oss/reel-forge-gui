import unittest

class TestClient(unittest.TestCase):
    def test_imports(self):
        import grpc
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
