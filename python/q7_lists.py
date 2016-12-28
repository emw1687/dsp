# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.
    """
    try:
        count = 0
        for word in words:
            if len(word) > 1:
                if word[0] == word [-1]:
                    count = count + 1
            else:
                continue
        return count
    except:
        raise NotImplementedError

"""
match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
#3
match_ends(['', 'x', 'xy', 'xyx', 'xx'])
#2
match_ends(['aaa', 'be', 'abc', 'hello'])
#1
"""


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
    """
    try:
        xwords = []
        otherwords = []
        allwords = []
        for word in words:
            if word[0] == 'x':
                xwords.append(word)
            else:
                otherwords.append(word)
        xwords.sort(), otherwords.sort()
        allwords.extend(xwords), allwords.extend(otherwords)
        print allwords
    except:
        raise NotImplementedError

"""
front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
#['xaa', 'xzz', 'axx', 'bbb', 'ccc']
front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
#['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
#['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
"""


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].
    """
    try: print sorted(tuples, key=lambda tuple: tuple[-1])
    except: raise NotImplementedError

"""
sort_last([(1, 3), (3, 2), (2, 1)])
#[(2, 1), (3, 2), (1, 3)]
sort_last([(2, 3), (1, 2), (3, 1)])
#[(3, 1), (1, 2), (2, 3)]
sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
#[(2, 2), (1, 3), (3, 4, 5), (1, 7)]
"""


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.
    """
    try:
        removed = []
        for index, value in enumerate(nums):
            if index == 0:
                removed.append(value)
            elif value == nums[index - 1]:
                continue
            else:
                removed.append(value)
        print removed
    except:
        raise NotImplementedError

"""
remove_adjacent([1, 2, 2, 3])
#[1, 2, 3]
remove_adjacent([2, 2, 3, 3, 3])
#[2, 3]
remove_adjacent([3, 2, 3, 3, 3])
#[3, 2, 3]
remove_adjacent([])
#[]
"""


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.
    """
    try:
        both = []
        both.extend(list1), both.extend(list2)
        both.sort()
        print both
    except:
        raise NotImplementedError

"""
linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
#['aa', 'bb', 'cc', 'xx', 'zz']
linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
#['aa', 'bb', 'cc', 'xx', 'zz']
linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
#['aa', 'aa', 'aa', 'bb', 'bb']
"""
