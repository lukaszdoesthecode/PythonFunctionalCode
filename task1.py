import unittest


def is_in_list_rec(x, T, pos=None):
    """
    Function checking if the variable x is inside the list T.
    :param x: (any) Parameter of any type to be searched in the list T.
    :param T: (list of any) List of variables/objects to be searched for x.
    :param pos: (int) Initialization of the holder for the length of the list.
    :return: (boolean) Boolean value communicating if the value is inside the list.
    """
    if not isinstance(T, list):
        raise TypeError('T should be a list')

    if pos == None:
        pos = 0

    if pos == len(T):
        return False
    elif T[pos] == x and pos < len(T):
        return True
    else:
        return is_in_list_rec(x, T, pos+1)


# Task 2
def binary_search(T, x, start, end):
    """
    The function checks whether the given value is in the given range of the sorted array and returns its index.
    :param T: (list of any) List of any variables/objects to be investigated.
    :param x: (any) Variable/object to be searched inside the list.
    :param start: (int)
    :param end: (int)
    :return: (int or None) Index of the found element in the array. In case there is no such value - returns None.
    """
    if not isinstance(T, list):
        raise TypeError('T should be a list')
    if not isinstance(start, int):
        raise TypeError('Start should be an integer.')
    if not isinstance(end, int):
        raise TypeError('End should be an integer.')
    if start < 0:
        raise ValueError('Start should not be a negative number.')
    if end < 0:
        raise ValueError('End should not be a negative number.')

    if start > end:
        return None

    center = (start+end)//2

    if T[center] == x:
        return center
    elif T[center] > x:
        return binary_search(T, x, start, center - 1)
    else:
        return binary_search(T, x, center + 1, end)


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

