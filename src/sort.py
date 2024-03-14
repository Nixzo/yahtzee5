"""sort.py"""


def insertion_sort(ulist):
    """ Insertion sort """
    for i in range(1, ulist.size()):
        key = ulist.get(i)
        j = i - 1
        while j >= 0 and ulist.get(j) > key:
            ulist.set(j + 1, ulist.get(j))
            j -= 1
        ulist.set(j + 1, key)


def recursive_insertion(ulist, n=None):
    """
    Rekursivt sortering på ulist, upp till index n.
    Returnerar den sorterade ulist.
    """
    if n is None:
        n = ulist.size()
    if n <= 1:
        return ulist
    recursive_insertion(ulist, n - 1)
    key = ulist.get(n - 1)
    j = n - 2

    # Kontrollera om det är en tupel innan loopen
    if isinstance(key, tuple):
        while j >= 0 and ulist.get(j)[1] > key[1]:  # jämför poängen
            ulist.set(j + 1, ulist.get(j))
            j -= 1
    else:
        while j >= 0 and ulist.get(j) > key:
            ulist.set(j + 1, ulist.get(j))
            j -= 1

    ulist.set(j + 1, key)
    return ulist
