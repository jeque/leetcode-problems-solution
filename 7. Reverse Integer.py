class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            res = int('-'+str(x)[::-1].strip('0').replace("-",''))
        elif x>0:
            res = int(str(x)[::-1].strip('0'))
        else:
            res = 0
        return res if (-(2**31))<res<((2**31)-1) else 0