import unittest
from task1 import is_in_list_rec, binary_search


class TestIsInListRec(unittest.TestCase):
    def test_first_case_is_in_list_rec(self):
        x = 0
        T = [-2, 1, 1.0, 3, 8]
        result = is_in_list_rec(x, T)
        self.assertEqual(result, False)

    def test_second_case_is_in_list_rec(self):
        x = 1
        T = [-2, 1, 1.0, 3, 8]
        result = is_in_list_rec(x, T)
        self.assertEqual(result, True)

    def test_third_case_is_in_list_rec(self):
        T = []
        x = T
        result = is_in_list_rec(x, T)
        self.assertEqual(result, False)

    def test_fourth_case_is_in_list_rec(self):
        T = 6
        x = 4
        with self.assertRaises(TypeError):
            result = is_in_list_rec(x, T)


class TestBinarySearch(unittest.TestCase):
    def test_first_case_binary_search(self):
        T = [-2, 1, 1.0, 3, 8]
        x = 0
        start = 0
        end = len(T) - 1
        result = binary_search(T, x, start, end)
        self.assertEqual(result, None)

    def test_second_case_binary_search(self):
        T = [-2, 1, 1.0, 3, 8]
        x = -2
        start = 0
        end = len(T) - 1
        result = binary_search(T, x, start, end)
        self.assertEqual(result, 0)

    def test_third_case_binary_search(self):
        T = 'test'
        x = -2
        start = 0
        end = len(T) - 1
        with self.assertRaises(TypeError):
            binary_search(T, x, start, end)

    def test_fourth_case_binary_search(self):
        T = [-2, 1, 1.0, 3, 8]
        x = -2
        start = -5
        end = len(T) - 1
        with self.assertRaises(ValueError):
            binary_search(T, x, start, end)


if __name__ == '__main__':
    unittest.main()
