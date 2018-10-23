class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_n = n * (n+1) / 2
        nums_sum = sum(nums)
        MissOne = int(sum_n - nums_sum)
        return MissOne