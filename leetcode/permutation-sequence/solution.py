class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # numbers
        nums = [str(i) for i in range(1, n + 1)]
        # (n - 1)!
        p = 1
        for i in range(2, n):
            p *= i
        res = ''
        for i in range(n - 1):
            j = (k-1)//p
            k -= j * p
            p //= n - i - 1
            res += nums.pop(j)
        res += nums[0]
        return res


def test(n, k, exp):
    str = Solution().getPermutation(n, k)
    postfix = '' if str == exp else 'FAILED!!!'
    print('%d %d --> %s %s' % (n, k, str, postfix))

if __name__ == '__main__':
    test(3, 1, '123')
    test(4, 8, '2143')
