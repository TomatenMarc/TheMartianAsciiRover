import unittest

from . import hex_alphabet


class TestHexAlphabet(unittest.TestCase):

    def test_length_of_hex_alphabet(self):
        length = len(hex_alphabet)
        self.assertEqual(16, length)

    def test_check_index_of_0(self):
        index = hex_alphabet.index("0")
        self.assertEqual(0, index)

    def test_check_index_of_1(self):
        index = hex_alphabet.index("1")
        self.assertEqual(1, index)

    def test_check_index_of_2(self):
        index = hex_alphabet.index("2")
        self.assertEqual(2, index)

    def test_check_index_of_3(self):
        index = hex_alphabet.index("3")
        self.assertEqual(3, index)

    def test_check_index_of_4(self):
        index = hex_alphabet.index("4")
        self.assertEqual(4, index)

    def test_check_index_of_5(self):
        index = hex_alphabet.index("5")
        self.assertEqual(5, index)

    def test_check_index_of_6(self):
        index = hex_alphabet.index("6")
        self.assertEqual(6, index)

    def test_check_index_of_7(self):
        index = hex_alphabet.index("7")
        self.assertEqual(7, index)

    def test_check_index_of_8(self):
        index = hex_alphabet.index("8")
        self.assertEqual(8, index)

    def test_check_index_of_9(self):
        index = hex_alphabet.index("9")
        self.assertEqual(9, index)

    def test_check_index_of_a(self):
        index = hex_alphabet.index("a")
        self.assertEqual(10, index)

    def test_check_index_of_b(self):
        index = hex_alphabet.index("b")
        self.assertEqual(11, index)

    def test_check_index_of_c(self):
        index = hex_alphabet.index("c")
        self.assertEqual(12, index)

    def test_check_index_of_d(self):
        index = hex_alphabet.index("d")
        self.assertEqual(13, index)

    def test_check_index_of_e(self):
        index = hex_alphabet.index("e")
        self.assertEqual(14, index)

    def test_check_index_of_f(self):
        index = hex_alphabet.index("f")
        self.assertEqual(15, index)
