import math


def sort(lst, left, right, cmp_func=None):
    if left >= right:
        return
    if right - left < 20:
        insertion_sort(lst, left, right, cmp_func)
    else:
        quick_sort(lst, left, right, cmp_func)


def insertion_sort(lst, left, right, cmp_func=None):
    for i in range(left + 1, right + 1):
        for j in range(i, 0, -1):
            if cmp_func(lst[j-1], lst[j]) if cmp_func else lst[j-1] < lst[j]:
                break
            swap(lst, j, j-1)


def quick_sort(lst, left, right, cmp_func=None):
    if left < right:
        p = partition(lst, left, right, cmp_func)
        sort(lst, left, p - 1, cmp_func)
        sort(lst, p + 1, right, cmp_func)


def partition(lst, left, right, cmp_func=None):
    pivot = lst[right]
    i = left
    for j in range(left, right):
        if cmp_func(lst[j], pivot) if cmp_func else lst[j] < pivot:
            swap(lst, i, j)
            i += 1
    swap(lst, i, right)
    return i


def select(lst, left, right):
    diff = right - left

    if diff < 1:
        return left

    if diff < 2:
        if lst[left] > lst[left + 1]:
            swap(lst, left, left + 1)
        return left

    if diff < 4:
        if lst[left] > lst[left + 1]:
            swap(lst, left, left + 1)
        if lst[left] > lst[left + 2]:
            swap(lst, left, left + 2)
        if diff == 3 and lst[left + 1] > lst[left + 3]:
            swap(lst, left + 1, left + 3)
        return left + 1

    # 5 items
    if lst[left] > lst[left + 1]:
        swap(lst, left, left + 1)
    if lst[left + 2] > lst[left + 3]:
        swap(lst, left + 2, left + 3)
    if lst[left] > lst[left + 2]:
        swap(lst, left, left + 2)
    if lst[left + 2] < lst[left + 4]:  # 3 < 5
        if lst[left + 1] < lst[left + 3]:  # 2 < 4
            if lst[left + 1] < lst[left + 2]:  # 2 < 3
                return left + 2
            else:
                if lst[left + 1] < lst[left + 4]:  # 2 < 5
                    return left + 1
                else:
                    return left + 4
        else:
            if lst[left + 3] < lst[left + 4]:
                return left + 3
            else:
                return left + 4
    else:
        if lst[left + 1] < lst[left + 2]:
            if lst[left + 1] < lst[left + 4]:
                return left + 4
            else:
                return left + 1
        else:
            return left + 2


def swap(lst, a, b):
    if a == b:
        return
    lst[a], lst[b] = lst[b], lst[a]


def mid_element(lst, left, right):
    # for 5 or less elements just get median
    if right - left < 5:
        return lst[select(lst, left, right)].left

    # otherwise move the medians of five-element subgroups to the first n/5 positions
    for i in range(left, right, 5):
        # get the median of the i'th five-element subgroup
        sub_right = i + 4
        if sub_right > right:
            sub_right = right
        median5 = select(lst, i, sub_right)
        swap(lst, int((i - left) / 5), median5)

    # compute the median of the n/5 medians-of-five
    return mid_element(lst, left, left + math.ceil((right - left) / 5))

