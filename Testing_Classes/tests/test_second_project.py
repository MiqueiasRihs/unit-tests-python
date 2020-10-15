import unittest

from second_project import Counter


class EasyTestCase(unittest.TestCase):
    def setUp(self):
        self.counter = Counter()

    def test_easy_input(self):
        self.assertEqual(self.counter.get_value(), 0)

    def test_easy_input_two(self):
        self.counter.clear()
        self.assertEqual(self.counter.get_value(), 0)
    
    def tearDown(self):
        self.counter = None