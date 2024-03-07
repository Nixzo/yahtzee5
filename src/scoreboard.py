"""
Detta är Scoreboard-modulen.
"""

from src.hand import Hand
from src.rules import (
    Ones, Twos, Threes, Fours, Fives, Sixes,
    ThreeOfAKind, FourOfAKind, Yahtzee, Chance,
    FullHouse, SmallStraight, LargeStraight
)


class Scoreboard:
    """
    Scoreboard klassen.
    """

    def __init__(self):
        self.points = {}
        self.used_rules = set()
        self.rules = [
            Ones(), Twos(), Threes(), Fours(), Fives(), Sixes(),
            ThreeOfAKind(), FourOfAKind(), Yahtzee(), Chance(),
            FullHouse(), SmallStraight(), LargeStraight()
        ]

    def add_points(self, rule_name: str, a_hand: Hand) -> None:
        """
        Lägger till poäng baserat på en regel och en hand.
        """
        if rule_name in self.used_rules:
            raise ValueError(f"Rule {rule_name} has already been used.")

        rule = next(
            (rule for rule in self.rules if rule.name == rule_name), None)

        #! Om regeln finns:
        if rule is not None:
            self.points[rule_name] = rule.points(a_hand)
            self.used_rules.add(rule_name)
        else:
            raise ValueError(f"No rule found with name {rule_name}")

    def get_total_points(self) -> int:
        """
        Returnerar den totala poängen.
        """
        return sum(points for points in self.points.values() if points != -1)

    def get_points(self, rule_name: str) -> int:
        """
        Returnerar poängen för en specifik regel.
        """
        return self.points.get(rule_name, 0)

    def get_highest_score(self, hand: Hand) -> str:
        """
        Returnerna highscore.

        Returns:
            str: Namnet på den mest poänggivande regeln.
        """
        max_points = 0
        best_rule = None
        for rule in self.rules:
            points = rule.points(hand)
            if points > max_points:
                max_points = points
                best_rule = rule.name
        return best_rule

    def finished(self) -> bool:
        """
        Kontrollerar om spelet är slut.
        """
        return len(self.used_rules) == len(self.rules)

    @staticmethod
    def from_dict(points: dict[str, int]) -> 'Scoreboard':
        """
        Skapar en Scoreboard-instans från en dictionary.
        Args:
        points (dict[str, int]): Dictionären som innehåller poängen för varje regel.
        Returns:
        Scoreboard: Den nyss skapade Scoreboard-instansen.
        """
        scoreboard_instance = Scoreboard()

        scoreboard_instance.points = points

        scoreboard_instance.used_rules = set(
            rule for rule, points in points.items() if points != -1)

        return scoreboard_instance
