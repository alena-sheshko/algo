"""
https://leetcode.com/problems/search-a-2d-matrix/
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix) - 1
        m = 0
        while n > 0 and matrix[n][m] > target:
            n -= 1
        while m < len(matrix[0]) - 1 and matrix[n][m] < target:
            m += 1
        return matrix[n][m] == target


def test(matrix, target, exp):
    for l in matrix:
        print('[%s]' % ', '.join(map(str, l)))

    print('%d --> ' % target, end='')
    res = Solution().searchMatrix(matrix, target)
    postfix = '' if res == exp else ' FAILED!!!'
    print('%s%s' % (res, postfix))

if __name__ == '__main__':
    test([[1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]], 3, True)

    test([[1,   3,  5,  7, 10, 11, 16, 20, 23, 30, 34, 50]], 15, False)
