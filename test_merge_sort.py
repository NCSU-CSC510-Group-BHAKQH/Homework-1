"""
Tests the merge_sort function in hw2_debugging.py
"""
import random

from hw2_debugging import merge_sort
from rand import random_array

#random array test case
def test_merge_sort_rand_array():
    """
    Tests the merge_sort function with randomly generated array.
    """
    # array_to_sort = random_array([None] * 20)
    array_to_sort = [3, 1, 2, -1]
    print()
    assert merge_sort(array_to_sort) == sorted(array_to_sort)

#sorted array test case
def test_merge_sort_sorted_array():
    """
    Tests the merge_sort function with an already sorted array.
    """
    array_to_sort = [random.randint(-1000,1000)]
    for _ in range(1000):
        array_to_sort.append(array_to_sort[-1]+random.randint(1,10))
    print(array_to_sort)
    assert merge_sort(array_to_sort) == array_to_sort

#duplicated member array test case
def test_merge_duplicate_rand_array():
    """
    Tests the merge_sort function with a duplicated random array.
    """
    array_to_sort = random_array([None] * 1000)
    for _ in range(10):
        j=random.randint(1,1000)
        array_to_sort[j]=array_to_sort[j-1]
    print(array_to_sort)
    assert merge_sort(array_to_sort) == sorted(array_to_sort)
