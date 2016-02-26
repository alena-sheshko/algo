import math


def quick_sort(list, left, right):
    if left < right:
        p = partition(list, left, right)
        quick_sort(list, left, p - 1)
        quick_sort(list, p + 1, right)


def partition(list, left, right):
    pivot = list[right]
    i = left
    for j in range(left, right - 1):
        if list[j] <= pivot:
            list[i], list[j] = list[j], list[i]
            i =+ 1
        list[i], list[right] = list[right], list[i]
    return i


def select(list, left, right):
    quick_sort(list, left, right)
    return left + int((right - left) / 2)


def median(list, left, right):
    # for 5 or less elements just get median
    if right - left < 5:
        return select(list, left, right)
    # otherwise move the medians of five-element subgroups to the first n/5 positions
    for i in range(left, right, 5):
        # get the median of the i'th five-element subgroup
        subRight = i + 4
        if subRight > right:
            subRight = right
        median5 = select(list, i, subRight)
        list[int((i-left)/5)], list[median5] = list[median5], list[int((i-left)/5)]

    # compute the median of the n/5 medians-of-five
    return median(list, left, left + math.ceil((right - left)/5))


if __name__ == '__main__':
    pass