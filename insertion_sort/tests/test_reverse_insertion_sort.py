from unittest import TestCase
from insertion_sort import reverse_insertion_sort


class TestInsertionSort(TestCase):

    def test_reverse_ordered_list(self):
        array = [7, 4, 1, 2, 0, 9, 8]
        inverse_ordered_list = reverse_insertion_sort.inverse_list_orderer(array)
        self.assertEqual(inverse_ordered_list[0], 9)
        self.assertEqual(inverse_ordered_list[1], 8)
        self.assertEqual(inverse_ordered_list[2], 7)
        self.assertEqual(inverse_ordered_list[3], 4)
        self.assertEqual(inverse_ordered_list[4], 2)
        self.assertEqual(inverse_ordered_list[5], 1)
        self.assertEqual(inverse_ordered_list[6], 0)