import random


def create_bitonic(n):
    lst = []
    div = random.randint(1, n - 1)
    for i in range(div):
        lst.append(i)
    l = lst[-1] - 1
    for i in range(l, l - n + div, -1):
        lst.append(i)
    return lst


def find_max(lst, lo, hi):
    if lo >= hi:
        return lo

    mid = lo + int((hi - lo)/2)
    if lst[mid + 1] > lst[mid]:
        return find_max(lst, mid + 1, hi)
    if lst[mid - 1] > lst[mid]:
        return find_max(lst, lo, mid - 1)
    return mid


def binary_search(lst, lo, hi, c, cmp_func):
    if lo >= hi:
        return c == lst[lo]

    mid = lo + int((hi - lo)/2)
    if c == lst[mid]:
        return True
    cmp_res = cmp_func(c, lst[mid])
    if not cmp_res:
        return binary_search(lst, mid + 1, hi, c, cmp_func)
    else:
        return binary_search(lst, lo, mid - 1, c, cmp_func)


def find(lst, c):
    mid = find_max(lst, 0, len(lst) - 1)
    return binary_search(lst, 0, mid, c, lambda x, y: x < y) or \
           binary_search(lst, mid + 1, len(lst) - 1, c, lambda x, y: x > y)


if __name__ == '__main__':
    array = create_bitonic(20)
    print('bitonic array: %s' % ','.join(map(str, array)))
    for i in range(10):
        num = random.randint(-20, 20)
        print('search for %d: %s' % (num, find(array, num)))
