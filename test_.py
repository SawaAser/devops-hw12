import unittest
from devopshw12.app import app


class Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_all_product(self):
        resource = self.app.get('/api/products')
        self.assertEqual(resource.status_code, 200)


if __name__ == '__main__':
    unittest.main()
