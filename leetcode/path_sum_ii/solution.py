"""
https://leetcode.com/problems/path-sum-ii/
"""
import pprint


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if not root:
            return []

        return self.find_path(root, sum, [])

    def find_path(self, node, sum, path):
        if not node:
            return []
        if sum == node.val and not node.left and not node.right:
            return [path[:] + [node.val]]
        path.append(node.val)
        left = self.find_path(node.left, sum - node.val, path)
        right = self.find_path(node.right, sum - node.val, path)
        path.pop()
        return left + right


def test(lst, sum, exp) -> object:
    print('[%s], %d --> ' % (','.join(map(str, lst)), sum), end='')
    root = None
    if lst:
        root = TreeNode(lst[0])
        i = 1
        q = [root]
        while i < len(lst):
            node = q.pop(0)
            node.left = TreeNode(lst[i]) if lst[i] else None
            if node.left:
                q.append(node.left)
            i += 1
            if i == len(lst):
                break
            node.right = TreeNode(lst[i]) if lst[i] else None
            if node.right:
                q.append(node.right)
            i += 1
    res = Solution().pathSum(root, sum)
    pprint.pprint(res)
    if res != exp:
        print('FAILED')


if __name__ == '__main__':
    test([5,
          4, 8,
          11, None, 13, 4,
          7, 2, None, None, 5, 1], 22, [[5, 4, 11, 2], [5, 8, 4, 5]])
    test([], 0, [])
    test([1,
          2], 1, [])
    test([-2,
          None, -3], -5, [[-2, -3]])
    test([1,
          -2, -3,
          1, 3, -2, None,
          -1], -1, [[1, -2, 1, -1]])
