"""
https://leetcode.com/problems/single-number-iii/
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bit = 0
        for n in nums:
            bit ^= n
        bit &= -bit
        res = [0, 0]
        for n in nums:
            res[not bit & n] ^= n
        return res


def test(nums, exp):
    print('[%s] --> ' % ','.join(map(str, nums)), end='')
    res = Solution().singleNumber(nums)
    print('[%s]%s' % (','.join(map(str, res)), '' if sorted(exp) == sorted(res) else ' FAILED!!!'))


if __name__ == '__main__':
    test([1, 2, 1, 3, 2, 5], [3, 5])

