class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indice = []
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1::]:
                indice.append(i)
                indice.append(nums[i+1::].index((target-nums[i]))+i+1)
        return indice