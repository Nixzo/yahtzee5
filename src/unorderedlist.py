"""unorderedlist.py"""

from src.node import Node
from src.errors import MissingIndex, MissingValue


class UnorderedList:
    """UnorderedList klass"""

    def __init__(self):
        """
        Konstruktorn för UnorderedList-klassen. Skapar en tom lista.
        """
        self._head = None

    def is_empty(self):
        """
        Kontrollerar om listan är tom. Returnerar True om listan är tom, annars False.
        """
        return self._head is None

    def append(self, data):
        """
        Lägger till ett nytt element/nod sist i listan.
        """
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node

    def size(self):
        """
        Returnerar antalet element i listan. En tom lista har storleken 0.
        """
        current = self._head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        """
        Söker efter data i listan. Returnerar True om datan finns i listan, annars False.
        """
        current = self._head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def remove(self, data):
        """
        Tar bort första förekomsten av data i listan.
        Returnerar True om datan togs bort, annars False.
        """
        current = self._head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self._head = current.next
                return
            previous = current
            current = current.next
        raise MissingValue("Value not found in list.")

    def get(self, index):
        """
        Returnerar värdet på index. Om index inte finns, lyfter MissingIndex exception.
        """
        current = self._head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next

        raise MissingIndex("Index out of range.")

    def set(self, index, data):
        """
        Skriver över element med ny data som finns på index.
        Om index inte finns, lyfter MissingIndex exception.
        """
        current = self._head
        count = 0
        while current:
            if count == index:

                current.data = data
                return
            count += 1
            current = current.next

        raise MissingIndex("Index out of range.")

    def index_of(self, data):
        """
        Om data finns i listan, returnerar dess index.
        Om värdet inte finns, lyfter MissingValue exception.
        """
        current = self._head
        count = 0
        while current:
            if current.data == data:
                return count
            count += 1
            current = current.next

        raise MissingValue("Value not found in list.")

    def print_list(self):
        """
        Skriver ut listans innehåll.
        """
        current = self._head
        while current:
            print(current.data)
            current = current.next

    def __iter__(self):
        """
        Gör UnorderedList itererbar.
        """
        current = self._head
        while current:
            yield current.data
            current = current.next
