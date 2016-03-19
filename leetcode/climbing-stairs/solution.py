"""
https://leetcode.com/problems/climbing-stairs/
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f0 = f1 = 1
        while n > 1:
            f0, f1 = f1, f0 + f1
            n -= 1
        return f1


def test(n, exp):
    res = Solution().climbStairs(n)
    print('{} --> {}{}'.format(n, res, '' if res == exp else ' FAILED!!!'))


if __name__ == '__main__':
    test(1, 1)
    test(2, 2)
    test(10, 89)
