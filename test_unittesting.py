import unittest

class LearningCase(unittest.TestCase):
	# test have to start with test_
    def test_starting_out(self):
        self.assertEqual(1, 1)

class TestCase(unittest.TestCase):
	def test_foo(self):
		self.assertTrue(True)



if __name__ == "__main__":
	# unit_test have a main function to start them
    unittest.main()



