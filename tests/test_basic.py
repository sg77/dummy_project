import unittest
from format_cli.utils import normalize_keys

class TestUtils(unittest.TestCase):

    def test_normalize_simple(self):
        data = {'A': 1}
        res = normalize_keys(data)
        self.assertEqual(res, {'a': 1})

    def test_nested(self):
        data = {'A': {'B': 2}}
        res = normalize_keys(data)
        self.assertIn('a', res)
        self.assertIn('b', res['a'])

    def test_list(self):
        data = {'A': [{'B': 1}, {'C': 2}]}
        res = normalize_keys(data)
        self.assertEqual(res['a'][0]['b'], 1)

    # incomplete test
    def test_edge(self):
        pass

if __name__ == '__main__':
    unittest.main()
