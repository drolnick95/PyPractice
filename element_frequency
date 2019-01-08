import string
import random
import time

# Iterate through each item and sum its occurrences. Results are returned in the 'counts' dictionary
def count_occurrences_naive(arr):
    counts = {}
    for item in arr:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


# Uses the Binary Search method to find the last occurrence of an item. The number of occurrences of each item
# will equal the index of the last occurrence minus the index of the first occurrence (+ 1). The next item's first
# occurrence will be the last occurrence's index + 1. Loops until the end of the array is reached. Results are returned
# in the 'counts' dictionary
def count_occurrences_better(arr):
    array_end = len(arr) -1
    start = 0
    counts = {}
    while start <= array_end:
        item = arr[start]
        last = find_last_occurrence2(arr, array_end, start, item, array_end)
        counts[item] = (last - start) + 1
        start = last+1
    return counts

# Uses a binary search method to find the last occurrence of the item in the array
def find_last_occurrence(arr, high, low, item, array_end):
    if (high>=low):
        mid = (high + low) // 2

    # We found it! This item is the target and the next item not the target (or its the end of the array)
    if mid == array_end and arr[mid] == item:
        return mid
    if item < arr[mid+1] and arr[mid] == item:
        return mid

    # Too far in the list
    elif arr[mid] > item:
        return find_last_occurrence(arr, mid - 1, low, item, array_end)

    # We are not yet to the last occurrence of the target item
    else:
        return find_last_occurrence(arr, high, mid + 1, item, array_end)

    # The item was not found. We should not reach this point, since we know every target occurs at least once.
    return -1

# Ths is the iterative version of the above code
def find_last_occurrence2(arr, high, low, item, array_end):
    while low <= high:
        mid = (high + low) // 2
        if mid == array_end and arr[mid] == item:
            return mid
        if item < arr[mid + 1] and arr[mid] == item:
            return mid
        elif arr[mid] > item:
            high = mid -1
        else:
            low = mid + 1

# Generate a random array of chars. Using default array size of 1,000 to display time differences
def generate_array (length = 1000):
    long_arr = ''
    for i in range(length):
        long_arr += random.choice(string.ascii_lowercase)
    return sorted(long_arr)


if __name__ == '__main__':

    arr = ['a', 'b', 'b', 'b', 'b', 'b', 'd', 'h', 'h', 'h', 'p']
    correct_counts = {'a': 1, 'b': 5, 'd': 1, 'h': 3, 'p': 1}

    try:
        start = time.time()
        naive = count_occurrences_naive(arr)
        end = time.time()
        assert naive == correct_counts
        print ('Naive count PASSED!')
        print ('Time Elapsed: {} seconds\n'.format(end - start))
    except (AssertionError):
        print('Naive count FAILED')

    try:
        start2 = time.time()
        better = count_occurrences_better(arr)
        end2 = time.time()
        assert better == correct_counts
        print ('Better count PASSED!')
        print ('Time Elapsed: {} seconds\n'.format(end - start))
    except (AssertionError):
        print('Better count FAILED')

    long_arr = generate_array()
    try:
        better_start = time.time()
        better2 = count_occurrences_better(long_arr)
        better_end = time.time()
        better_time = better_end - better_start

        naive_start = time.time()
        naive2 = count_occurrences_naive(long_arr)
        naive_end = time.time()
        naive_time = naive_end - naive_start

        assert better2 == naive2
        print ('Random String test PASSED!')
        print ('Better Method took: {} seconds'.format(better_time))
        print ('Naive Method took: {} seconds'.format(naive_time))
        print ('The Better Method was {} seconds faster'.format(naive_time-better_time))
    except (AssertionError):
        print ('Random String test FAILED')
