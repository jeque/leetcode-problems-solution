class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        if not str:
            return ""
        lowerstr = ""
        for i in str:
            lower = i
            if ord(lower) <= 91 and ord(lower) >= 65:
                lower = chr(ord(lower) + 32)
            lowerstr += lower
        return lowerstr
                