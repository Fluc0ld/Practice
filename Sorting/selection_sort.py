from random import randint
from time import time


def create_array(length: int = 10, maxint: int = 50) -> list:
    """
    Create randomized array of length 'length',
    array integers are of range 0, maxint
    """
    new_arr = [randint(0, maxint) for _ in range(length)]
    return new_arr

def selection_sort(arr: list) -> list:
    for i in range(0, len(arr) - 1):
        curr_min_indx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[curr_min_indx]:
                curr_min_indx = j

        arr[i], arr[curr_min_indx] = arr[curr_min_indx], arr[i]  # swap

    return arr

def benchmark(s_time: list = [10, 100, 1000, 10000]) -> None:
    select_exec_time = []  # select sort time
    built_in_exec_time = []  # built-in sort time

    for length in s_time:
        array_to_check = create_array(length, length)

        built_time_1 = time()
        build_sorted = sorted(array_to_check)  # sort with built in
        built_time_2 = time()
        built_in_exec_time.append(built_time_2 - built_time_1)

        select_time_1 = time()
        select_sorted = selection_sort(array_to_check)  # sort with select sort
        select_time_2 = time()
        select_exec_time.append(select_time_2 - select_time_1)

    for i, current_num in enumerate(s_time):
        print(f"Num - {current_num}\tBuilt-In - {built_in_exec_time[i]:.4f}\tBubble Sort - {select_exec_time[i]:.4f}")


array = create_array()
print(array)
sel_sort = selection_sort(array)
print(sel_sort)

print(array is sel_sort)

benchmark()
