class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p = 0
        #numsN = sorted(nums)
        if 0 in nums:
            for i in range(len(nums)):
                if nums[i] == 0:
                    p += 1
                    continue
                nums[i-p] = nums[i]
            for i in range(len(nums[:-p]),len(nums)):
                nums[i] = 0