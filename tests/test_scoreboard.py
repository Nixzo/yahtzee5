"""
Detta modul innehåller tester för Scoreboard-klassen.
"""
import unittest
from src.hand import Hand
from src.scoreboard import Scoreboard


class TestScoreboard(unittest.TestCase):
    """
    Testklass för Scoreboard-klassen.
    """

    def setUp(self):
        """
        Skapar en ny instans av Scoreboard-klassen inför varje test.
        """
        self.scoreboard = Scoreboard()

    def test_add_points(self):
        """
        Testar att add_points()-metoden lägger till rätt poäng för en regel.
        """
        hand = Hand([1, 2, 3, 4, 5])
        self.scoreboard.add_points('Ones', hand)
        self.assertEqual(self.scoreboard.get_points('Ones'), 1)

    def test_add_points_existing_rule(self):
        """
        Testar att add_points()-metoden lyfter ett undantag när poäng läggs till
        för en regel som redan har poäng.
        """
        hand = Hand([1, 2, 3, 4, 5])
        self.scoreboard.add_points('Ones', hand)
        with self.assertRaises(ValueError):
            self.scoreboard.add_points('Ones', hand)
