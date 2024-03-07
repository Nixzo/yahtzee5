"""node.py"""


class Node:
    """node klass"""

    def __init__(self, data=None):
        """
        Konstruktorn för Node-klassen. Tar emot data som argument och sätter nästa nod till None.
        """
        self.data = data  # !! Lagrar datan i noden
        self.next = None  # Referens till nästa nod, sätts till None till att börja med
