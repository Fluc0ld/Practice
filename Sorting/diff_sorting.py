from random import randint
from time import time
from prettytable import PrettyTable


def create_array(length: int = 10, maxint: int = 50) -> list:
    """
    Create randomized array of length 'length',
    array integers are of range 0, maxint
    """
    new_arr = [randint(0, maxint) for _ in range(length)]
    return new_arr

def is_sorted(arr: list) -> bool:
    sorted_arr = sorted(arr)

    return arr == sorted_arr

def speed_test(to_check, extra_args, to_record: list) -> list:
    start_time_ = time()
    to_check(extra_args)
    end_time = time()
    to_record.append(end_time - start_time_)

    return to_record

def bubble_sort(arr: list) -> list:
    swapped = True

    while swapped:
        swapped = False
        for val in range(1, len(arr)):
            if arr[val-1] > arr[val]:
                arr[val], arr[val-1] = arr[val-1], arr[val]
                swapped = True

    return arr

def selection_sort(arr: list) -> list:
    for i in range(0, len(arr) - 1):
        curr_min_indx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[curr_min_indx]:
                curr_min_indx = j

        arr[i], arr[curr_min_indx] = arr[curr_min_indx], arr[i]  # swap

    return arr

def insert_sort(arr: list) -> list:
    for sort_len in range(1, len(arr)):
        curr_item = arr[sort_len]  # next unsorted item
        insert_inx = sort_len  # current index of item

        # iterate until we reach correct insert spot
        while insert_inx > 0 and curr_item < arr[insert_inx - 1]:
            arr[insert_inx] = arr[insert_inx - 1]  # shift
            insert_inx +=- 1  # decrement insert spot

        arr[insert_inx] = curr_item

    return arr

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        left_arr_indx = 0
        right_arr_indx = 0
        merge_arr_indx = 0

        while left_arr_indx < len(left_arr) and right_arr_indx < len(right_arr):
            if left_arr[left_arr_indx] < right_arr[right_arr_indx]:
                arr[merge_arr_indx] = left_arr[left_arr_indx]
                left_arr_indx += 1
            else:
                arr[merge_arr_indx] = right_arr[right_arr_indx]
                right_arr_indx += 1
            merge_arr_indx += 1

        while left_arr_indx < len(left_arr):
            arr[merge_arr_indx] = left_arr[left_arr_indx]
            left_arr_indx += 1
            merge_arr_indx += 1

        while right_arr_indx < len(right_arr):
            arr[merge_arr_indx] = right_arr[right_arr_indx]
            right_arr_indx += 1
            merge_arr_indx += 1

    return arr

def benchmark(s_time: list = [10, 100, 1000, 10000]) -> None:
    insert_time = []
    bubble_time = []
    selection_time = []
    merge_time = []

    for length in s_time:
        array_to_check = create_array(length, length)

        speed_test(bubble_sort, array_to_check, bubble_time)
        speed_test(selection_sort, array_to_check, selection_time)
        speed_test(insert_sort, array_to_check, insert_time)
        speed_test(merge_sort, array_to_check, merge_time)

    result_table = PrettyTable(["Number", "Bubble", "Selection", "Insert", "Merge"])

    for i, length in enumerate(s_time):
        result_table.add_row([length, f"{bubble_time[i]:05f}", f"{selection_time[i]:05f}", f"{insert_time[i]:05f}",
                              f"{merge_time[i]:05f}"])

    print(result_table)

if __name__ == "__main__":
    benchmark()
