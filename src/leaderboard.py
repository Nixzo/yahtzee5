"""leaderboard.py"""

from src.unorderedlist import UnorderedList


class Leaderboard:
    """leaderboard klass"""

    def __init__(self, entries=None):
        """
        Initierar Leaderboard med en oordnad lista av inlägg.
        """
        self.entries = UnorderedList()
        if entries is not None:
            for entry in entries:
                self.entries.append(entry)

    @classmethod
    def load(cls, filename):
        """
        Laddar inlägg från en given fil, eller skapar en ny fil om den inte finns.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                entries = [line.strip().split(',') for line in file]
        except FileNotFoundError:
            # Skapar en ny fil om den inte finns
            with open(filename, 'a+', encoding='utf-8') as file:
                entries = []  # Inga inlägg att läsa in eftersom filen är ny
        return cls(entries)

    def save(self, filename):
        """
        Sparar inlägg till en given fil.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            for node in self.entries:
                file.write(f"{node[0]},{node[1]}\n")

    def add_entry(self, name, score):
        """
        Lägger till ett inlägg med givet namn och poäng.
        """
        self.entries.append((name, score))

    def remove_entry(self, index):
        """
        Tar bort inlägget på givet index.
        """
        self.entries.remove(index)

    def print_leaderboard(self):
        """
        Skriver ut alla inlägg i leaderboard.
        """
        self.entries.print_list()
