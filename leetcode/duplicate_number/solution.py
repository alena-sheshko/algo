"""
https://leetcode.com/problems/find-the-duplicate-number/
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        finder = 0
        # tortoise and hare step
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        while slow != finder:
            slow = nums[slow]
            finder = nums[finder]
        return slow


def test(nums, exp):
    print('%s --> ' % ','.join(map(str, nums)), end='')
    res = Solution().findDuplicate(nums)
    postfix = '' if exp == res else ' FAILED!!!'
    print('%d%s' % (res, postfix))


if __name__ == '__main__':
    test([4, 2, 3, 2, 3], 3)
    test([6, 2, 4, 3, 7, 1, 5, 7], 7)
    test([1, 2, 3, 4, 5, 6, 7, 8, 9, 5], 5)
