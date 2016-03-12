"""
https://leetcode.com/problems/house-robber/
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1 = 0
        p2 = nums[0] if nums else 0
        for i in range(1, len(nums)):
            p1, p2 = p2, max(p1 + nums[i], p2)
        return p2


def test(nums, exp):
    res = Solution().rob(nums)
    print('[%s] --> %d%s' % (','.join(map(str, nums)), res, '' if exp ==res else ' FAILED!!!'))


if __name__ == '__main__':
    test([1, 98, 1, 45, 100, 50, 2, 2], 200)
    test([], 0)
