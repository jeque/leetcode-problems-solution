class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """   
        k = len(digits) - 1
        while k >= 0:
            if digits[k] == 9:
                digits[k] = 0
                if k == 0:
                    digits.insert(0,1)
            else:
                digits[k] += 1
                break
            k -= 1
        return digits