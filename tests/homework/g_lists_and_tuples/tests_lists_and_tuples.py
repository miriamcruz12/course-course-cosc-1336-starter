import unittest
from src.homework.g_lists_and_tuples import lists

class TestListFunctions(unittest.TestCase):
    def test_get_lowest_list_value(self):
        data = [8, 10, 1, 50, 20]
        result = list.get_lowest_list_value(data)
        self.assertEqual(result, 1)

    def test_get_highest_list_value(self):
        data = [8, 10, 1, 50, 20]
        result = lists.get_highest_list_value(data)
        self.assertEqual(result, 50) 