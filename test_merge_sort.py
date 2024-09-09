"""
Tests the merge_sort function in hw2_debugging.py
"""
from hw2_debugging import merge_sort
from hw2_debugging import recombine
from rand import random_array

def test_merge_sort_rand_array():
    array_to_sort = random_array([None] * 100) 
    print(array_to_sort)
    assert merge_sort(array_to_sort) == sorted(array_to_sort)
