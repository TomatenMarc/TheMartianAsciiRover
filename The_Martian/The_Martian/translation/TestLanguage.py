import unittest

from The_Martian.translation.translator import translate_to_hex


class TestTextToHexadecimal(unittest.TestCase):

    def test_no_0x_in_string(self):
        hex_string = translate_to_hex("test")
        self.assertNotIn("0x", hex_string)

    def test_single_letter_A(self):
        hex_string = translate_to_hex("A")
        self.assertEqual("41", hex_string)

    def test_single_letter_B(self):
        hex_string = translate_to_hex("B")
        self.assertEqual("42", hex_string)

    def test_single_letter_C(self):
        hex_string = translate_to_hex("C")
        self.assertEqual("43", hex_string)

    def test_single_letter_a(self):
        hex_string = translate_to_hex("a")
        self.assertEqual("61", hex_string)

    def test_single_letter_b(self):
        hex_string = translate_to_hex("b")
        self.assertEqual("62", hex_string)

    def test_single_letter_c(self):
        hex_string = translate_to_hex("c")
        self.assertEqual("63", hex_string)

    def test_space(self):
        hex_string = translate_to_hex(" ")
        self.assertEqual("20", hex_string)

    def test_word_hi(self):
        hex_string = translate_to_hex("hi")
        self.assertEqual("6869", hex_string)

    def test_word_status(self):
        hex_string = translate_to_hex("STATUS")
        self.assertEqual("535441545553", hex_string)

    def test_sentence_how_alive(self):
        hex_string = translate_to_hex("HOW ALIVE?")
        self.assertEqual("484f5720414c4956453f", hex_string)
