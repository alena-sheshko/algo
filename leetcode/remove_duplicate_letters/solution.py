"""
https://leetcode.com/problems/remove-duplicate-letters/
"""


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        q = {}
        v = {}
        for ch in s:
            q[ch] = q.get(ch, 0) + 1
            v[ch] = False

        stack = []
        for ch in s:
            if not v[ch]:
                while stack and stack[-1] > ch and q[stack[-1]] > 0:
                    p = stack.pop()
                    v[p] = False
                stack.append(ch)
                v[ch] = True
            q[ch] -= 1
        return ''.join(stack)


def test(s, exp):
    res = Solution().removeDuplicateLetters(s)
    print('{} --> {}{}'.format(s, res, '' if res == exp else ' FAILED!!!'))

if __name__ == '__main__':
    test("bcabc", "abc")
    test("cbacdcbc", "acdb")
