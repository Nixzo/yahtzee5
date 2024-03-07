"""
test_hand.py
"""
import unittest
from src.hand import Hand


class TestHand(unittest.TestCase):
    """
    Testklass för Hand-klassen.
    """

    def setUp(self):
        """
        Skapar en ny instans av Hand.
        """
        self.hand = Hand([1, 2, 3, 4, 5])

    def test_roll_with_indexes(self):
        """
        Testar att roll()-metoden slår om rätt tärningar när en lista med index ges.
        """
        self.hand.roll([0, 2, 4])
        new_values = str(self.hand).split(', ')
        for value in new_values:
            self.assertTrue(1 <= int(value) <= 6)

    def test_roll_without_indexes(self):
        """
        Testar att roll()-metoden slår om alla tärningar.
        """
        original_values = str(self.hand).split(', ')
        self.hand.roll()
        new_values = str(self.hand).split(', ')
        self.assertNotEqual(original_values, new_values)

    def test_to_list(self):
        """
        Testar att __str__()-metoden returnerar en lista med tärningarnas värde.
        """
        values = str(self.hand).split(', ')
        self.assertEqual(values, ['1', '2', '3', '4', '5'])
