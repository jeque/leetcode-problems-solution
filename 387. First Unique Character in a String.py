class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string
        letters = [chr(i) for i in range(97,123)]
        index=[s.index(j) for j in letters if s.count(j) == 1]
        return min(index) if len(index) > 0 else -1