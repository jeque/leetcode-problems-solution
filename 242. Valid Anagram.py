class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lower_alpha = [chr(i) for i in range(97,123)]
        s_array = []
        t_array = []
        for i in range(26):
            s_array.append(s.count(lower_alpha[i]))
            t_array.append(t.count(lower_alpha[i]))
        if s_array == t_array:
            return True
        else:
            return False