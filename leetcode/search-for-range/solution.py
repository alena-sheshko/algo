class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = right = -1
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        else:
            return [left, right]  # not found

        find_inx = mid
        lo_inx = lo
        hi_inx = hi
        if not find_inx or nums[find_inx - 1] != target:
            left = find_inx
        else:
            lo = lo_inx
            hi = find_inx - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target and (mid == 0 or nums[mid - 1] < target):
                    break
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            left = mid

        if find_inx == len(nums) - 1 or nums[find_inx + 1] != target:
            right = find_inx
        else:
            lo = find_inx + 1
            hi = hi_inx
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] > target):
                    break
                elif nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid - 1
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
