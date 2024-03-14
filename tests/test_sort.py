"""
Detta modul innehåller tester för recursive_insertion!
"""

import unittest
from src.sort import recursive_insertion
from src.unorderedlist import UnorderedList


class TestSort(unittest.TestCase):
    """test"""

    def test_recursive_insertion_sort_integers(self):
        """Testar att sorterar en lista med heltal."""
        ulist = UnorderedList()
        for i in [3, 5, 111, 1, 34, 0, 11]:
            ulist.append(i)
        sorted_list = recursive_insertion(ulist)
        self.assertEqual(list(sorted_list), [0, 1, 3, 5, 11, 34, 111])

    def test_recursive_insertion_sort_strings(self):
        """Testar att sorterar en lista med strängar."""
        ulist = UnorderedList()
        for i in ['hej', '22', 'haha', '2', '34', '222']:
            ulist.append(i)
        sorted_list = recursive_insertion(ulist)
        self.assertEqual(list(sorted_list), [
                         '2', '22', '222', '34', 'haha', 'hej'])
