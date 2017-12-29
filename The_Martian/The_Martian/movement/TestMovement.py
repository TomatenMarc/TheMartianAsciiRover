import unittest

from The_Martian.movement.move import get_index_pair, get_possible_movement, get_alternative_movement


class TestIndexPairs(unittest.TestCase):

    def test_simple_pair1(self):
        x, y = "a", "0"
        ind_x, ind_y = get_index_pair(x, y)
        self.assertEqual(10, ind_x)
        self.assertEqual(0, ind_y)

    def test_simple_pair2(self):
        x, y = "0", "f"
        ind_x, ind_y = get_index_pair(x, y)
        self.assertEqual(0, ind_x)
        self.assertEqual(15, ind_y)


class TestPossibleMovement(unittest.TestCase):

    def test_simple1(self):
        ind_x, ind_y = 0, 4
        possible = get_possible_movement(ind_x, ind_y)
        self.assertEqual(12, possible)

    def test_simple2(self):
        ind_x, ind_y = 4, 8
        possible = get_possible_movement(ind_x, ind_y)
        self.assertEqual(12, possible)

    def test_simple3(self):
        ind_x, ind_y = 8, 4
        possible = get_possible_movement(ind_x, ind_y)
        self.assertEqual(4, possible)

    def test_simple4(self):
        ind_x, ind_y = 4, 9
        possible = get_possible_movement(ind_x, ind_y)
        self.assertEqual(11, possible)

    def test_simple5(self):
        ind_x, ind_y = 9, 0
        possible = get_possible_movement(ind_x, ind_y)
        self.assertEqual(9, possible)

    def test_simple6(self):
        ind_x, ind_y = 15, 0
        possible = get_possible_movement(ind_x, ind_y)
        self.assertEqual(15, possible)


class TestAlternativeMovement(unittest.TestCase):

    def test_simple1(self):
        ind_x, ind_y = 0, 4
        possible = get_alternative_movement(ind_x, ind_y)
        self.assertEqual(4, possible)

    def test_simple2(self):
        ind_x, ind_y = 4, 8
        possible = get_alternative_movement(ind_x, ind_y)
        self.assertEqual(4, possible)

    def test_simple3(self):
        ind_x, ind_y = 8, 4
        possible = get_alternative_movement(ind_x, ind_y)
        self.assertEqual(12, possible)

    def test_simple4(self):
        ind_x, ind_y = 4, 9
        possible = get_alternative_movement(ind_x, ind_y)
        self.assertEqual(5, possible)

    def test_simple5(self):
        ind_x, ind_y = 9, 0
        possible = get_alternative_movement(ind_x, ind_y)
        self.assertEqual(7, possible)

    def test_simple6(self):
        ind_x, ind_y = 15, 0
        possible = get_alternative_movement(ind_x, ind_y)
        self.assertEqual(1, possible)
