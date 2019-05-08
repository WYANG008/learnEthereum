import unittest
import sys

sys.path.append('src')
import trie

class Test(unittest.TestCase):
    # ## convert byte to nibbles
    # def test_bin_to_nibbles(self):
    #     result = trie.bin_to_nibbles("\x01\x01\x02")
    #     print result

    # ## pack a terminator 16 to the end of the key
    # def test_with_terminator(self):
    #     result = trie.with_terminator([0,1,0,1,0,2])
    #     print result

    def test_pack_nibbles(self):
        result = trie.pack_nibbles([0,1,0,1,0,2,16])
        print str(result)

if __name__ == '__main__':
    unittest.main()
# def bin_to_nibbles(s):
#     """convert string s to nibbles (half-bytes)

#     >>> bin_to_nibbles("")
#     []
#     >>> bin_to_nibbles("h")
#     [6, 8]
#     >>> bin_to_nibbles("he")
#     [6, 8, 6, 5]
#     >>> bin_to_nibbles("hello")
#     [6, 8, 6, 5, 6, 12, 6, 12, 6, 15]
#     """
#     res = []
#     for x in s:
#         res += divmod(ord(x), 16)
#     return res