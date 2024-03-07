"""
Modul för rules.py
"""

from abc import ABC, abstractmethod
from src.hand import Hand


class Rule(ABC):
    """
    Abstrakt Rule klass.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def points(self, the_hand: Hand) -> int:
        """
        Beräknar poäng baserat på hand.
        """


class SameValueRule(Rule):
    """
    SameValueRule klassen.
    """

    def __init__(self, value: int, name: str) -> None:
        """
        Initera objektet med det angivna namnet och värdet.
        """
        super().__init__(str(name))
        self.value = value

    def points(self, the_hand: Hand) -> int:
        """
        Beräknar poäng för tärningar av samma värde i hand.
        """
        values = [die.get_value() for die in the_hand.dice]
        return values.count(self.value) * self.value or 0


class Ones(SameValueRule):
    """
    Initera objektet med det angivna namnet och värdet.
    """

    def __init__(self):
        """
        Ones
        """
        super().__init__(1, 'Ones')


class Twos(SameValueRule):
    """
    Initera objektet med det angivna namnet och värdet.
    """

    def __init__(self):
        """
        Twos
        """
        super().__init__(2, 'Twos')


class Threes(SameValueRule):
    """
    Initera objektet med det angivna namnet och värdet.
    """

    def __init__(self):
        """
        Threees
        """
        super().__init__(3, 'Threes')


class Fours(SameValueRule):
    """
    Initera objektet med det angivna namnet och värdet.
    """

    def __init__(self):
        """
        Fours
        """
        super().__init__(4, 'Fours')


class Fives(SameValueRule):
    """
    Initera objektet med det angivna namnet och värdet.
    """

    def __init__(self):
        """
        Fives
        """
        super().__init__(5, 'Fives')


class Sixes(SameValueRule):
    """
    Initera objektet med det angivna namnet och värdet.
    """

    def __init__(self):
        """
        Sixes
        """
        super().__init__(6, 'Sixes')


class ThreeOfAKind(Rule):
    """
    ThreeOfAKind klassen.
    """

    def __init__(self):
        """
        ThreeOfAKind
        """
        super().__init__("Three Of A Kind")

    def points(self, the_hand: Hand) -> int:
        """
        Beräknar poäng för tre tärningar av samma värde i hand.
        """
        values = [die.get_value() for die in the_hand.dice]
        for value in set(values):
            if values.count(value) >= 3:
                return sum(values)
        return 0


class FourOfAKind(Rule):
    """
    FourOfAKind klassen.
    """

    def __init__(self):
        """
        FourOfAKind
        """
        super().__init__("Four Of A Kind")

    def points(self, the_hand: Hand) -> int:
        """
        Beräknar poäng för fyra tärningar av samma värde i hand.
        """
        values = [die.get_value() for die in the_hand.dice]
        for value in set(values):
            if values.count(value) >= 4:
                return sum(values)
        return 0


class Yahtzee(Rule):
    """
    Yahtzee klassen.
    """

    def __init__(self):
        """
        Yahtzee
        """
        super().__init__("Yahtzee")

    def points(self, the_hand: Hand) -> int:
        """
        Beräknar poäng för en Yahtzee i hand.
        """
        values = [die.get_value() for die in the_hand.dice]
        if len(set(values)) == 1:
            return 50
        return 0


class Chance(Rule):
    """
    chans klass.
    """

    def __init__(self):
        """
        Chance
        """
        super().__init__('Chance')

    def points(self, the_hand: Hand) -> int:
        """
        Beräkna den totala poängen för handen genom att summera värdena på alla tärningar.

        :param the_hand: Handen för vilken poängen ska beräknas.
        :type the_hand: Hand
        :return: Den totala poängen för handen.
        :rtype: int
        """
        return sum(die.get_value() for die in the_hand.dice)


class FullHouse(Rule):
    """
    Initialize the object with the specified parameters.
    """

    def __init__(self):
        """
        FullHouse
        """
        super().__init__('Full House')

    def points(self, the_hand: Hand) -> int:
        """
        Beräkna poängen för den givna handen baserat på tärningsvärdena.

        :param the_hand: Hand-objektet som representerar tärningsvärdena.
        :return: Ett heltal som representerar de beräknade poängen.
        """
        values = [die.get_value() for die in the_hand.dice]
        if sorted(values.count(die) for die in set(values)) == [2, 3]:
            return 25
        return 0


class SmallStraight(Rule):
    """
    Initialize the object with the specified parameters.
    """

    def __init__(self):
        """
        SmallStraight
        """
        super().__init__('Small Straight')

    def points(self, the_hand: Hand) -> int:
        """
        Beräknar poängen för den angivna handen.
        Parametrar:
            the_hand (Hand): Handen för vilken poängen ska beräknas.
        Returnerar:
            int: Totala poängen beräknad för handen.
        """
        values = sorted(die.get_value() for die in the_hand.dice)
        if (set([1, 2, 3, 4]).issubset(values) or
            set([2, 3, 4, 5]).issubset(values) or
                set([3, 4, 5, 6]).issubset(values)):
            return 30
        return 0


class LargeStraight(Rule):
    """
    Initialize the object with the specified parameters.
    """

    def __init__(self):
        """
        LargeStraight
        """
        super().__init__('Large Straight')

    def points(self, the_hand: Hand) -> int:
        """
        Beräkna poängen för en given hand i ett tärningsspel.
        Parametrar:
            the_hand (Hand): Handen med tärningar att beräkna poäng för.
        Returnerar:
            int: De totala poängen som beräknats för handen.
        """
        values = sorted(die.get_value() for die in the_hand.dice)
        if values in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]:
            return 40
        return 0
