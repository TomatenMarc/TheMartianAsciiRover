import unittest

from The_Martian.sequencing.sequenzer import split_into_sequences, add_start_and_end_position


class TestPositioning(unittest.TestCase):

    def test_hex_string_starts_and_ends_with_0(self):
        hex_string = "ab"
        hex_string = add_start_and_end_position(hex_string)
        self.assertEqual("0ab0", hex_string)


class TestSequencer(unittest.TestCase):

    def test_simple_string1(self):
        hex_string = "ab"
        precursor, successor = split_into_sequences(hex_string)
        self.assertEqual("a", precursor)
        self.assertEqual("b", successor)

    def test_simple_string2(self):
        hex_string = "123"
        precursor, successor = split_into_sequences(hex_string)
        self.assertEqual("12", precursor)
        self.assertEqual("23", successor)

    def test_simple_string3(self):
        hex_string = "12ab45"
        precursor, successor = split_into_sequences(hex_string)
        self.assertEqual("12ab4", precursor)
        self.assertEqual("2ab45", successor)


class TestSequencingAndPositioning(unittest.TestCase):

    def test_positioning_and_sequencing_1(self):
        hex_string = "ab"
        hex_string = add_start_and_end_position(hex_string)
        precursor, successor = split_into_sequences(hex_string)
        self.assertEqual("0ab", precursor)
        self.assertEqual("ab0", successor)

    def test_positioning_and_sequencing_2(self):
        hex_string = "010"
        hex_string = add_start_and_end_position(hex_string)
        precursor, successor = split_into_sequences(hex_string)
        self.assertEqual("0010", precursor)
        self.assertEqual("0100", successor)

    def test_positioning_and_sequencing_3(self):
        hex_string = "4243"
        hex_string = add_start_and_end_position(hex_string)
        precursor, successor = split_into_sequences(hex_string)
        self.assertEqual("04243", precursor)
        self.assertEqual("42430", successor)
