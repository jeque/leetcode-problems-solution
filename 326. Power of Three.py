class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        if n == 1:
            return True
        val = 1
        while val < n:
            val *= 3
            if val == n:
                return True
        return False