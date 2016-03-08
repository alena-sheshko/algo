"""
https://leetcode.com/problems/next-permutation/
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                # reverse array after pivot
                j = len(nums) - 1
                k = i + 1
                while j > k:
                    nums[j], nums[k] = nums[k], nums[j]
                    j -= 1
                    k += 1
                # find replacement
                lo = i + 1
                hi = len(nums) - 1
                while lo <= hi:
                    mid = lo + ((hi - lo) >> 1)
                    if nums[mid] > nums[i]:
                        if nums[i] >= nums[mid - 1]:
                            nums[mid], nums[i] = nums[i], nums[mid]
                            break
                        else:
                            hi = mid - 1
                    else:
                        lo = mid + 1
                break
            i -= 1
        else:
            nums.reverse()


def test(nums, exps):
    print('%s --> ' % ','.join(map(str, nums)), end="")
    Solution().nextPermutation(nums)
    if nums == exps:
        print(','.join(map(str, nums)))
    else:
        print('%s (FAILED!!!)' % ','.join(map(str, nums)))

if __name__ == '__main__':
    test([3, 2, 1], [1, 2, 3])
    test([1, 2, 3], [1, 3, 2])
    test([1, 1, 5], [1, 5, 1])
    test([4, 2, 1, 3], [4, 2, 3, 1])
    test([1, 3, 2], [2, 1, 3])
    test([5, 5, 5], [5, 5, 5])
    test([1, 3, 2, 0], [2, 0, 1, 3])
    test([5, 4, 7, 5, 3, 2], [5, 5, 2, 3, 4, 7])
    test([2, 3, 1], [3, 1, 2])
    test([2, 2, 0, 4, 3, 1], [2, 2, 1, 0, 3, 4])
    test([2, 1, 2, 2, 2, 2, 2, 1], [2, 2, 1, 1, 2, 2, 2, 2])
