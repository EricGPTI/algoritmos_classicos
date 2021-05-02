from unittest import TestCase
from insertion_sort import insertion_sort


class TestInsertionSort(TestCase):

    def test_ordered_list(self):
        array = [7, 4, 1, 2, 0, 9, 8]
        ordered_list = insertion_sort.list_orderer(array)
        self.assertEqual(ordered_list[0], 0)
        self.assertEqual(ordered_list[1], 1)
        self.assertEqual(ordered_list[2], 2)
        self.assertEqual(ordered_list[3], 4)
        self.assertEqual(ordered_list[4], 7)
        self.assertEqual(ordered_list[5], 8)
        self.assertEqual(ordered_list[6], 9)