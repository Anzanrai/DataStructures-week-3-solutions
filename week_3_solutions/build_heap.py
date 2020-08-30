# python3
import math

def build_heap(data, n):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    iterator_count = math.ceil((n-1)/2)
    swaps = []
    for i in range(iterator_count, -1, -1):
        shift_down(i, data, n, swaps)
    return swaps
    # swaps = []
    # for i in range(len(data)):
    #    for j in range(i + 1, len(data)):
    #        if data[i] > data[j]:
    #            swaps.append((i, j))
    #            data[i], data[j] = data[j], data[i]
    # return swaps
#    for i in range(iterator_count)


def left_child(i):
    return 2*i+1

def right_child(i):
    return 2*i+2

def shift_down(i, data, size, swaps):
    min_index = i
    l = left_child(i)
    if l <= size-1 and data[l] < data[min_index]:
        min_index = l
    r = right_child(i)
    if r <= size-1 and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        shift_down(min_index, data, size, swaps)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data, n)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
