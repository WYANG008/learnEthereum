import unittest
import sys

sys.path.append('src')
import rlp

class TestRlp(unittest.TestCase):
    def test_encode(self):
        result = rlp.encode(['hello'])
        print result

if __name__ == '__main__':
    unittest.main()