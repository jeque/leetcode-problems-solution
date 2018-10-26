class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = nums[0]
        sum_value = max_value
        for i in range(1,len(nums)):
            if sum_value < 0:
                sum_value = 0
            sum_value += nums[i]
            if sum_value > max_value:
                max_value = sum_value
        return max_value