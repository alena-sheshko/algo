import math


def quick_sort(lst, left, right, cmp_func=None):
    if left < right:
        p = partition(lst, left, right, cmp_func)
        quick_sort(lst, left, p - 1, cmp_func)
        quick_sort(lst, p + 1, right, cmp_func)


def partition(lst, left, right, cmp_func=None):
    pivot = lst[right]
    i = left
    for j in range(left, right - 1):
        cmp = cmp_func(lst[j], pivot) if cmp_func else lst[j] <= pivot
        if cmp:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
        lst[i], lst[right] = lst[right], lst[i]
    return i


def select(lst, left, right):
    quick_sort(lst, left, right)
    return left + int((right - left) / 2)


def mid_element(lst, left, right):
    # for 5 or less elements just get median
    if right - left < 5:
        return select(lst, left, right)

    # otherwise move the medians of five-element subgroups to the first n/5 positions
    for i in range(left, right, 5):
        # get the median of the i'th five-element subgroup
        subright = i + 4
        if subright > right:
            subright = right
        median5 = select(lst, i, subright)
        lst[int((i - left) / 5)], lst[median5] = lst[median5], lst[int((i - left) / 5)]

    # compute the median of the n/5 medians-of-five
    return mid_element(lst, left, left + math.ceil((right - left) / 5))

