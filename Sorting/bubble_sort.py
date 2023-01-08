from random import randint
from time import time


def create_array(length: int = 10, maxint: int = 50) -> list:
    """
    Create randomized array of length 'length',
    array integers are of range 0, maxint
    """
    new_arr = [randint(0, maxint) for _ in range(length)]
    return new_arr


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


def is_sorted(arr: list) -> bool:
    sorted_arr = sorted(arr)

    return arr == sorted_arr


def benchmark(tme: list = [10, 100, 1000, 10000]) -> None:
    bubble_exec_time = []  #  bubble sort time
    built_in_exec_time = []  #  built-in sort time

    for length in tme:
        array_to_check = create_array(length, length)

        built_time_1 = time()
        build_sorted = sorted(array_to_check)  # sort with built in
        built_time_2 = time()
        built_in_exec_time.append(built_time_2 - built_time_1)

        bubble_time_1 = time()
        bubble_sorted = bubble_sort(array_to_check)  # sort with bubble sort
        bubble_time_2 = time()
        bubble_exec_time.append(bubble_time_2 - bubble_time_1)

    for i, current_num in enumerate(tme):
        print(f"Num - {current_num}\tBuilt-In - {built_in_exec_time[i]:.4f}\tBubble Sort - {bubble_exec_time[i]:.4f}")


array = create_array()
print(array)
bubble = bubble_sort(array)
print(bubble)

print(is_sorted(array))

benchmark()
