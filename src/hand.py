"""
hand.py
"""
from src.die import Die


class Hand:
    """
    Hand klassen.
    """

    def __init__(self, dice_values=None):
        """
        Konstruktorn för Hand-klassen. Skapar en ny instans av Hand.
        """

        self.dice = [Die(value) for value in dice_values] if dice_values else [
            Die() for _ in range(5)]

    def roll(self, indexes=None):
        """
        Kastar om tärningarna på de angivna indexpositionerna.
        Om inga index ges, kastas alla tärningar om.

        Parametrar:
        indexes (list<int>, optional): En lista med indexpositioner
        för tärningarna som ska kastas om.
        Standardvärdet är None.
        """
        indexes = indexes if indexes else range(len(self.dice))
        for index in indexes:
            self.dice[index].roll()

    def to_list(self):
        """
        Returnerar en lista med värdet på alla tärningar i handen.

        Returnerar:
            list: En lista med tärningarnas värden.
        """
        return [die.get_value() for die in self.dice]

    def __str__(self):
        """
        Returnerar en komma-separerad sträng med värdet på alla tärningar i handen.

        Returnerar:
        str: En komma-separerad sträng med tärningarnas värden.
        """
        return ', '.join(str(die) for die in self.dice)
