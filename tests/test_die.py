"""
test_die.py
"""
import unittest
import random
from src.die import Die


class TestDie(unittest.TestCase):
    """
    Testklass för Die-klassen.
    """

    def setUp(self):
        """
        Skapar en ny instans av Die-klassen inför varje test.
        """
        self.die = Die()

    def test_initial_value(self):
        """
        Testar att det initiala värdet på tärningen ligger inom det tillåtna intervallet.
        """
        self.assertTrue(Die.MIN_ROLL_VALUE <=
                        self.die.get_value() <= Die.MAX_ROLL_VALUE)

    def test_roll(self):
        """
        Testar att roll()-metoden.
        """
        random.seed(1)
        self.die = Die()
        expected_values = [5, 1, 3, 1, 4, 4, 4, 6, 4, 2]
        values = [self.die.roll() for _ in range(10)]
        self.assertEqual(values, expected_values)
        for value in values:
            self.assertTrue(Die.MIN_ROLL_VALUE <= value <= Die.MAX_ROLL_VALUE)

    def test_constructor_with_value(self):
        """
        Testar att konstruktorn korrekt sätter tärningens värde när ett giltigt värde ges.
        """
        die = Die(value=3)
        self.assertEqual(die.get_value(), 3)

    def test_constructor_with_invalid_value(self):
        """
        Testar att konstruktorn sätter tärningens värde till MAX_ROLL_VALUE när
        ett ogiltigt värde ges.
        """
        die = Die(value=88)
        self.assertEqual(die.get_value(), Die.MAX_ROLL_VALUE)

    def test_get_name(self):
        """
        Testar att get_name()-metoden returnerar korrekt namn.
        """
        value_names = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six"
        }
        for i in range(1, 7):
            die = Die(value=i)
            self.assertEqual(die.get_name(), value_names[i])

    def test_eq(self):
        """
        Testar att __eq__()-metoden korrekt jämför två Die-objekt.
        """
        die1 = Die(value=3)
        die2 = Die(value=3)
        # de borde vara lika eftersom deras värden är lika
        self.assertEqual(die1, die2)

        die3 = Die(value=4)
        # de borde inte vara lika eftersom deras värden är olika
        self.assertNotEqual(die1, die3)
