import unittest
from first_project import avg

class EasyTestCase(unittest.TestCase):
    
    def test_easy_input(self):
        self.assertEqual(avg(1, 2, 3), 2)

    def test_easy_input_two(self):
        pass


if __name__ == '__main__':
    unittest.main()
    