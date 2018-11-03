class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = [int(x) for x in list(str(n))]
        value = sum([x**2 for x in l])

        while value >= 0:

            value = sum([x**2 for x in l])
            l = [int(x) for x in list(str(value))]
            if value == 1:
                return True
                break
            
            elif value in (37, 58, 145):
                return False
                break