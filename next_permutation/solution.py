class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        #find pivot
        pivot = len(nums) - 1
        i = pivot - 1
        while i >= 0:
            if nums[i] < nums[pivot]:
                pivot = i
                break
            pivot = i
            i -= 1

        # replace pivot
        if i >= 0:
            if pivot == len(nums) - 2:
                nums[pivot], nums[pivot + 1] = nums[pivot + 1], nums[pivot]
            else:
                i = len(nums) - 1
                half = pivot + int((i-pivot)/2)
                changed = False
                while i > half:
                    if not changed and nums[pivot] < nums[i]:
                        nums[pivot], nums[i] = nums[i], nums[pivot]
                        changed = True
                    #reverse list
                    opposite = pivot + len(nums) - i
                    nums[i], nums[opposite] = nums[opposite], nums[i]
                    i -= 1
                if not changed:
                    i = half + 1
                    while i < len(nums):
                        if nums[pivot] < nums[i]:
                            nums[pivot], nums[i] = nums[i], nums[pivot]
                            break
                        i += 1
        else:
            nums.reverse()

def test(nums):
   print('%s --> ' % ','.join(map(str, nums)), end="")
   Solution().nextPermutation(nums)
   print(','.join(map(str, nums)))

if __name__ == '__main__':
    test([3, 2, 1])
    test([1, 2, 3])
    test([1, 1, 5])
    test([4,2,1,3])
    test([1, 3, 2])
    test([5, 5, 5])
    test([1, 3, 2, 0])
    test([5,4,7,5,3,2])
    test([2, 3, 1])
    test([2,2,0,4,3,1])
    test([2,1,2,2,2,2,2,1])
