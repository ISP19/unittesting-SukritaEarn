def unique(lst):
    """Return a list containing only the first occurence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        list: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"])
    ['b', 'a']
    >>> unique([])
    []
    >>> unique([8, 8, 8, 8, 8])
    [8]
    >>> unique([1, "a", 2, "b"])
    [1, 'a', 2, 'b']
    >>> unique([[1, 2], [2, 1]])
    [[1, 2], [2, 1]]
    >>> unique([["a", "b"], ["a", "b"], ["a"], ["b"], ["ab"]])
    [['a', 'b'], ['a'], ['b'], ['ab']]
    >>> unique([1, 2, 2, 4, [1,2,3], 1, [1,2,3]])
    [1, 2, 4, [1, 2, 3]]
    >>> unique([0, 0, 0, 1, 1, 0, 0, 2, 2, 0, 0, 1, 1, 0, 3, 2, 2, 2, 0, 0, 0, 3, 3, 2, 2, 2, 2, 0, 0, 3, 3, 0, 0, 4, 0, 0, 0, 5, 5, 5])
    [0, 1, 2, 3, 4, 5]
    >>> unique(list)
    Traceback (most recent call last):
      File "listutil.py", line 31, in unique
        raise ValueError("Input must be a list")
    ValueError: Input must be a list
    >>> unique("[]")
    Traceback (most recent call last):
      File "listutil.py", line 36, in unique
        raise ValueError("Input must be a list")
    ValueError: Input must be a list
    """
    if type(lst) != list:
        raise ValueError("Input must be a list")
    unique_list = []
    for x in lst:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
