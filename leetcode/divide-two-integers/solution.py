"""
httpsleetcode.comproblemsdivide-two-integers
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        divd = abs(dividend)
        abs_divs = abs(divisor)
        res = 0
        while divd >= abs_divs:
            count = -1
            divs = abs_divs
            while divd >= divs:
                divs <<= 1
                count += 1
            res += 1 << count
            divd -= divs >> 1
        return -min(res, 2147483648) if (dividend > 0) ^ (divisor > 0) else min(res, 2147483647)


def test(dividend, divisor, exp):
    res = Solution().divide(dividend, divisor)
    print('{}/{} --> {}{}'.format(dividend, divisor, res, '' if res == exp else ' FAILED!!!'))

if __name__ == '__main__':
    test(15, 10, 1)
    test(15, 5, 3)
    test(15, 7, 2)
    test(1, -1, -1)
    test(-1, -1, 1)
    test(-2147483648, -1, 2147483647)
