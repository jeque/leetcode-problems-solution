class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums_copy = nums[:]
        for i in range(len(nums_copy)):
            if i+k >=length:
                index = (i+k)%length
            else:
                index = i+k
            nums[index] = nums_copy[i]