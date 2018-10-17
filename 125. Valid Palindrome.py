class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #验证字符串是否由字母和数字组成，并将大写字母转换为小写
        PaliS = [i.lower() for i in s if i.isalnum()]
        #验证是否是回文 
        return PaliS[:int(len(PaliS)/2)] == PaliS[int((len(PaliS)+1)/2):][::-1]