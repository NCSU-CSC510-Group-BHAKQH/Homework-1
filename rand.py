"""
Helper 'random' methods for merge-sort impl in hw2_debugging.py.
"""
import subprocess


def random_array(arr):
    """
    Generates and returns a random array to be sorted.
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
