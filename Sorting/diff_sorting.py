from random import randint
from time import time


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
    """
    Apply the bubble sorting algorithm to the input array
    """
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

def benchmark(s_time: list = [10, 100, 1000, 10000]) -> None:
    insert_time = []
    bubble_time = []
    selection_time = []

    for length in s_time:
        array_to_check = create_array(length, length)

        # bubble = bubble_sort(array_to_check)
        speed_test(bubble_sort, array_to_check, bubble_time)
        # selection = selection_sort(array_to_check)
        speed_test(selection_sort, array_to_check, selection_time)
        # insert = insert_sort(array_to_check)
        speed_test(insert_sort, array_to_check, insert_time)

    print("\nNumber \tBubble\tSelection\tInsert")
    print(40 * "_")
    for i, length in enumerate(s_time):
        print(f"{length:d}  \t{bubble_time[i]:0.5f} \t{selection_time[i]:0.5f} \t{insert_time[i]:0.5f}")

if __name__ == "__main__":
    benchmark()
