import unittest
from listutil import unique

class ListUtilTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], unique([]))
 
    def test_single_item_list(self):
        self.assertListEqual(['hi'], unique(['hi']))
        self.assertListEqual([8], unique([8]))

    def test_single_item_many_times_list(self):
        self.assertListEqual([3], unique([3, 3, 3]))
        self.assertListEqual(["e"], unique(["e", "e", "e", "e", "e"]))

    def test_two_items_list(self):
        self.assertListEqual([0, 1], unique([0, 1, 1, 1, 1, 0, 0, 1]))
        self.assertListEqual(["o", "x"], unique(["o", "x", "o", "x", "x", "o", "o", "o"]))

    def test_no_duplicate_list(self):
        self.assertListEqual(["E", "A", "R", "N"], unique(["E", "A", "R", "N"]))

    def test_many_items_list(self):
        self.assertListEqual([1, 2, 3, "a", "t"], unique([1, 1, 2, 2, 3, 3, 3, 3, "a", "t", "t", "a", "a", "t"]))

    def test_two_list_items_different_order(self):
        self.assertListEqual([[2, 3], [3, 2]], unique([[2, 3], [3, 2], [2, 3]]))
        self.assertListEqual([["c", "a", "r"], ["r", "a", "c"]], unique([["c", "a", "r"], ["r", "a", "c"]]))

    def test_not_list_argument(self):
        with self.assertRaises(ValueError):
            unique("not list")
        with self.assertRaises(ValueError):
            unique(["[1,2,3,4]"])
        with self.assertRaises(ValueError):
            unique(890)

if __name__ == '__main__':
    unittest.main()