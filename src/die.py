"""
die.py
"""
import random


class Die:
    """
    Tärnings klasssen.
    """
    MIN_ROLL_VALUE: int = 1
    MAX_ROLL_VALUE: int = 6

    def __init__(self,  value=None, die_name="Die",) -> None:
        """
        Konstruktorn för Die-klassen. Skapar en ny instans av Die.

        Parametrar:
        name (str, optional): Namnet på tärningen.
        value (int, optional): Det initiala värdet på tärningen.
        Om värdet är större än MAX_ROLL_VALUE, sätts det till MAX_ROLL_VALUE.
        Om värdet är mindre än MIN_ROLL_VALUE, sätts det till MIN_ROLL_VALUE.
        Om inget värde ges, genereras ett slumpmässigt värde.
        Standardvärdet är None.
        """
        self._value = value if value is not None else self.roll()
        self._value = min(
            max(self._value, Die.MIN_ROLL_VALUE), Die.MAX_ROLL_VALUE)
        self.die_name = die_name

    def get_name(self) -> str:
        """
        Returnerar namnet på tärningens värde.
        """
        value_names = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six"
        }
        return value_names.get(self.get_value())

    def get_value(self) -> int:
        """
        Hämtar värdet för objektet.
        """
        return self._value

    def roll(self) -> int:
        """
        Generera ett slumpmässigt värde mellan MIN_ROLL_VALUE och MAX_ROLL_VALUE.

        Returnerar:
            int: Det genererade slumpmässiga värdet.
        """
        self._value = random.randint(Die.MIN_ROLL_VALUE, Die.MAX_ROLL_VALUE)
        return self._value

    def __str__(self) -> str:
        """
        Returnerar en strängrepresentation av objektet.
        """
        return str(self.get_value())

    def __eq__(self, other):
        """
        Jämför detta Die-objekt med ett annat objekt.

        Returnerar:
            bool: True om det andra objektet också är en Die och har samma värde, False annars.
        """
        if isinstance(other, Die):
            return self._value == other._value
        if isinstance(other, int):
            return self._value == other
        return False
