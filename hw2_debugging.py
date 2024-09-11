"""
Python merge-sort implementation.
"""


def merge_sort(arr):
    """
    Core recursive merge-sort function.
    """
    if len(arr) == 1:
        return arr

    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Recombine function for merging left and right arrays together.
    """
    left_index, left_len = 0, len(left_arr)
    right_index, right_len = 0, len(right_arr)
    merge_index, merge_len = 0, (left_len + right_len)
    merge_arr = [None] * (merge_len)

    print(f"Left Arr: {left_arr}, Right Arr: {right_arr}")

    while left_index < left_len and right_index < right_len:
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[merge_index] = left_arr[left_index]
            merge_index += 1
            left_index += 1
        else:
            merge_arr[merge_index] = right_arr[right_index]
            merge_index += 1
            right_index += 1

    if left_index == left_len:
        for i in range(right_index, right_len):
            merge_arr[merge_index] = right_arr[i]
            merge_index += 1
    elif right_index == right_len:
        for i in range(left_index, left_len):
            merge_arr[merge_index] = left_arr[i]
            merge_index += 1

    return merge_arr
