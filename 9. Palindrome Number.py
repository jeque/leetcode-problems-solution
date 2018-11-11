class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0:
            return False
        if x>=0:
            string_one = str(x)
            string_two = string_one[::-1]
            if string_one == string_two:
                return True
            else:
                return False