"""
https://leetcode.com/problems/missing-number/
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (len(nums) * (len(nums) + 1))/2 - sum(nums)


def test(nums, exp):
        print('[%s] --> ' % ','.join(map(str, nums)), end='')
        res = Solution().missingNumber(nums)
        print('%d%s' % (res, '' if res == exp else ' FAILED!!!'))

if __name__ == '__main__':
    test([0, 1, 3], 2)