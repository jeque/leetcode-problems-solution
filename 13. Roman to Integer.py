class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer = 0
        before_roman = 0
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        rev_s = s[::-1]
        for i in range(len(s)):
            roman_int = roman_dict[rev_s[i]]
            if roman_int < before_roman:
                integer = integer - roman_int
            else:
                integer = integer + roman_int
            before_roman = roman_int
        return integer