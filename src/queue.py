"""queue.py"""


class Queue:
    """
    En klass för att representera en kö.
    """

    def __init__(self):
        """
        Initierar en ny kö.
        """
        self._items = []

    def is_empty(self):
        """
        Kontrollerar om kön är tom.

        Returnerar:
            bool: True om kön är tom, False annars.
        """
        return not self._items

    def enqueue(self, item):
        """
        Lägger till ett objekt i slutet av kön.

        Parametrar:
            item (objekt): Objektet som ska läggas till.
        """
        self._items.append(item)

    def dequeue(self):
        """
        Tar bort och returnerar objektet i början av kön.

        Returnerar:
            objekt: Objektet i början av kön.
            str: Meddelande om kön är tom.
        """
        try:
            return self._items.pop(0)
        except IndexError:
            return "Empty list."

    def peek(self):
        """
        Returnerar objektet i början av kön utan att ta bort det.

        Returnerar:
            objekt: Objektet i början av kön.
        """
        return self._items[0]

    def size(self):
        """
        Returnerar storleken på kön.

        Returnerar:
            int: Storleken på kön.
        """
        return len(self._items)

    def to_list(self):
        """
        Konverterar kön till en lista.

        Returnerar:
            list: En lista med objekten i kön.
        """
        return self._items

    @classmethod
    def from_list(cls, items):
        """
        Skapar en ny kö från en lista.

        Parametrar:
            items (list): En lista med objekten som ska läggas till i kön.

        Returnerar:
            Queue: En ny kö med objekten från listan.
        """
        queue = cls()
        for item in items:
            queue.enqueue(item)
        return queue
