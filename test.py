import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test(self):
        name='Saurabh'
        up=to_upper(name)
        self.assertEqual(up,'SAURABH')

if __name__ == '__main__':
    unittest.main()