"""
https://leetcode.com/problems/search-for-a-range/
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        else:
            if not nums or nums[lo] != target:
                return [-1, -1]  # not found

        if lo == hi and nums[lo] == target:
            return [lo, hi]

        left = right = mid
        lo_border = lo
        hi_border = hi
        if left > 0 and nums[left - 1] == target:
            lo = lo_border
            hi = left - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] == target and (mid == 0 or nums[mid - 1] < target):
                    break
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                mid = lo
            left = mid

        if right < len(nums) - 1 and nums[right + 1] == target:
            lo = right + 1
            hi = hi_border
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] > target):
                    break
                elif nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                mid = lo
            right = mid
        return [left, right]


def test(nums, target, exp):
    res = Solution().searchRange(nums, target)
    print('[{}], {} --> [{}]{}'.format(','.join(map(str, nums)), target, ','.join(map(str, res)),
                                       '' if res == exp else ' FAILED!!!'))

if __name__ == '__main__':
    test([5, 7, 7, 8, 8, 10], 8, [3, 4])
    test([], 1, [-1, -1])
    test([1], 1, [0, 0])
    test([2, 2], 2, [0, 1])
    test([0, 0, 0, 0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 8, 9, 9, 10, 10, 11, 11], 0, [0, 3])
    test([1, 4], 4, [1, 1])
    test([0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 8, 10, 10], 4, [10, 13])
