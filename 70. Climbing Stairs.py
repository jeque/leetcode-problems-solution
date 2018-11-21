class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0, 1, 2]
        def step(m):  
            if m >= len(memo):
                memo.append(step(m-1) + step(m-2))
            return memo[m]
        return step(n)